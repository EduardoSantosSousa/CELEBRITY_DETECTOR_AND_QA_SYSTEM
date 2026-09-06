import cv2
from io import BytesIO
import numpy as np

class InvalidImageError(ValueError):
    """Indicates that the uploaded file is not a valid image."""


def process_image(image_file):
    """ Validates the image, identifies the largest face, and returns the JPEG bytes."""

    in_memory_file = BytesIO()
    image_file.save(in_memory_file)
    image_bytes = in_memory_file.getvalue()

    if not image_bytes:
        raise InvalidImageError("The uploaded file is empty")

    image_array = np.frombuffer(image_bytes, dtype=np.uint8)
    image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

    if image is None:
        raise InvalidImageError("The uploaded file is not a valid image.")

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    face_cascade = cv2.CascadeClassifier(cascade_path)

    if face_cascade.empty():
        raise RuntimeError("Unable to load the face detector.")

    faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(40,40),)

    if len(faces) == 0:
        return image_bytes, None

    largest_face = max(faces, key=lambda rectangle: rectangle[2]* rectangle[3])
    x,y, width, height = largest_face
    cv2.rectangle(image, (x, y), (x + width, y+height), (0, 200, 0), 3)    

    encoding_succeeded, buffer = cv2.imencode(".jpg", image)
    if not encoding_succeeded:
        raise InvalidImageError("The image could not be processed")

    return buffer.tobytes(), tuple(int(value) for value in largest_face)
