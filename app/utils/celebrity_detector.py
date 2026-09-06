import base64
import json
import os
import re

import requests

class CelebrityDetectionError(RuntimeError):
    """Indicates a failure to identify a celebrity"""

class CelebrityDetector:
    def __init__(self, api_key=None, timeout=30):
        self.api_key = api_key or os.getenv("GROQ_API_KEY")
        self.api_url = "https://api.groq.com/openai/v1/chat/completions"
        self.model = os.getenv("GROQ_VISION_MODEL", "qwen/qwen3.6-27b")
        self.timeout = timeout

    def identify(self, image_bytes):
        if not self.api_key:
            raise CelebrityDetectionError(
                "The GROQ_API_KEY environment variable is not set."
            )

        encoded_image = base64.b64encode(image_bytes).decode("utf-8")
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type":"application/json",
        }
        payload = {
            "model": self.model,
            "messages": [
                {
                    "role":"user",
                    "content":[
                        {
                            "type":"text",
                            "text": (
                                "Identify the celebrity in this image. Return only a JSON "
                                "object with these exact string keys: full_name, profession, "
                                "nationality, famous_for, and top_achievements. Do not include "
                                "analysis, reasoning, Markdown, or additional keys. If you cannot "
                                "identify the person confidently, set full_name to Unknown and "
                                "briefly explain the uncertainty in famous_for."
                            ),
                        },
                        {
                            "type":"image_url",
                            "image_url":{
                                "url":f"data:image/jpeg;base64,{encoded_image}"
                            },
                        },
                    ],
                }
            ],
            "temperature": 0.2,
            "max_completion_tokens": 1024,
            "reasoning_effort": "none",
            "response_format": {"type": "json_object"},
        }

        try:
            response = requests.post(self.api_url, headers=headers, json=payload, timeout=self.timeout)
            response.raise_for_status()
            data = response.json()
            content = data["choices"][0]["message"]["content"].strip()
            details = self.parse_response(content)
        except requests.Timeout as error:
            raise CelebrityDetectionError(
                "Identification took longer than expected. Try again."
                                          ) from error
        except requests.RequestException as error:
            raise CelebrityDetectionError(
                "Unable to access the identification service."
            ) from error
        except (KeyError, IndexError, TypeError, ValueError) as error:
            raise CelebrityDetectionError(
                "The service returned a response in an unexpected format."
            ) from error

        name = details.get("full_name", "").strip()
        if not name or name.lower() == "unknown":
            return "It was not possible to identify the person with certainty.", ""

        player_info = self.format_details(details)
        return player_info, name

    @staticmethod
    def parse_response(content):
        """Parse the final JSON and defensively remove exposed reasoning."""
        sanitized = re.sub(
            r"<think>.*?</think>",
            "",
            content,
            flags=re.IGNORECASE | re.DOTALL,
        ).strip()
        sanitized = re.sub(r"^```(?:json)?\s*|\s*```$", "", sanitized).strip()
        details = json.loads(sanitized)
        if not isinstance(details, dict):
            raise ValueError("The identification response is not a JSON object.")
        return details

    @staticmethod
    def format_details(details):
        fields = (
            ("Profession", "profession"),
            ("Nationality", "nationality"),
            ("Famous for", "famous_for"),
            ("Top achievements", "top_achievements"),
        )
        return "\n\n".join(
            f"{label}:\n{str(details.get(key) or 'Not available').strip()}"
            for label, key in fields
        )

    @staticmethod
    def extract_name(content):
        expected_prefix = "- **full name**:"
        for line in content.splitlines():
            normalized_line = line.strip()
            if normalized_line.lower().startswith(expected_prefix):
                return normalized_line.split(":", maxsplit=1)[1].strip()
        return ""
