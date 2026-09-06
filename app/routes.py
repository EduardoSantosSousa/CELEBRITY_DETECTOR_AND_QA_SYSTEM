import base64
from flask import Blueprint, current_app, render_template, request
from app.utils.celebrity_detector import (CelebrityDetectionError, CelebrityDetector)
from app.utils.image_handler import InvalidImageError, process_image
from app.utils.qa_engine import QAEngine, QAEngineError

main = Blueprint("main", __name__)
ALLOWED_EXTENSIONS = {"jpg", "jpeg", "png", "webp"}

def is_allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

def page_state(**overrides):

    state = {
        "player_info": "",
        "player_name": "",
        "result_img_data":"",
        "user_question":"",
        "answer":"",
        "error":"",
    }

    state.update(overrides)
    return state


@main.route("/", methods=["GET", "POST"])
def index():
    state = page_state()

    if request.method == "GET":
        return render_template("Home.html", **state)

    action = request.form.get("action", "")

    if action == "identify":
        image_file = request.files.get("image")

        if image_file is None or not image_file.filename:
            state["error"] = "Select an image before submitting."
            return render_template("Home.html", **state), 400

        if not is_allowed_file(image_file.filename):
            state["error"] = "Invalid format. Upload a JPG, JPEG, PNG, or WEBP image."
            return render_template("Home.html", **state), 400

        try:
            image_bytes, face_box = process_image(image_file)

            if face_box is None:
                state["error"] = "No face was detected. Try another image."
                return render_template("Home.html", **state), 422

            detector = CelebrityDetector()
            player_info, player_name = detector.identify(image_bytes)
            state.update(player_info=player_info, player_name=player_name, result_img_data=base64.b64encode(image_bytes).decode("utf-8"),
            )
        except (InvalidImageError, CelebrityDetectionError) as error:
            state["error"] = str(error)
        except Exception:
            current_app.logger.exception("Unexpected failure during identification")
            state["error"] = "An unexpected error occurred while processing the image."

    elif action == "ask":
        state.update(
            player_name = request.form.get("player_name", "").strip(),
            player_info = request.form.get("player_info", "").strip(),
            result_img_data = request.form.get("result_img_data", "").strip(),
            user_question = request.form.get("question", "").strip(),
        )

        try:
            qa_engine = QAEngine()
            state["answer"] = qa_engine.ask_about_celebrity(state["player_name"], state["user_question"],)
        except QAEngineError as error:
            state["error"] = str(error)
        except Exception:
            current_app.logger.exception("Unexpected failure during the query")        
            state["error"] = "An unexpected error occurred while generating the response"
    else:
        state["error"] = "Invalid form action."

    if action == "identify" and state["player_name"]:
        return render_template("Detection_results.html", **state)

    if action == "ask":
        return render_template("Detection_results.html", **state)

    return render_template("Home.html", **state)


@main.app_errorhandler(413)
def file_too_large(_error):
    state = page_state(error="The image exceeds the 8 MB limit.")
    return render_template("Home.html", **state), 413




