import os 
import re

import requests

class QAEngineError(RuntimeError):
    """Indicates a failure to answer a question."""

class QAEngine:
    def __init__(self, api_key=None, timeout=30):
        self.api_key = api_key or os.getenv("GROQ_API_KEY")
        self.api_url = "https://api.groq.com/openai/v1/chat/completions"
        self.model = os.getenv("GROQ_TEXT_MODEL", "openai/gpt-oss-20b")
        self.timeout = timeout

    def ask_about_celebrity(self, name, question):
        if not self.api_key:
            raise QAEngineError(
                "The GROQ_API_KEY environment variable is not set"
            )

        clean_name = (name or "").strip()
        clean_question = (question or "").strip()

        if not clean_name:
            raise QAEngineError("Identify a celebrity before asking questions")
        if not clean_question:
            raise QAEngineError("Enter a question before sending")

        headers= {
            "Authorization":f"Bearer {self.api_key}",
            "Content-Type":"application/json",
        }

        payload = {
            "model": self.model,
            "messages": [
                {
                    "role":"system",
                    "content":(
                        "You answer questions about public figures concisely and accurately. "
                        "If a fact is uncertain, explicitly say that you are uncertain. "
                        "Write in clean plain text without Markdown, asterisks, headings, or "
                        "numbered steps. Start with a direct answer. If a list helps, use short "
                        "lines beginning with a bullet character. Keep the answer easy to scan."
                    ),
                },
                {
                    "role":"user",
                    "content":f"Celebrity: {clean_name} \nQuestion: {clean_question}",
                },
            ],
            "temperature": 0.3,
            "max_completion_tokens": 512,
            "reasoning_effort": "low",
            "reasoning_format": "hidden",
        }

        try:
            response = requests.post(self.api_url, headers=headers, json=payload, timeout=self.timeout)
            response.raise_for_status()
            data = response.json()
            content = data["choices"][0]["message"]["content"].strip()
            return self.clean_answer(content)

        except requests.Timeout as error:
            raise QAEngineError(
                "The response took longer than expected. Try again."
            ) from error
        except requests.RequestException as error:
            raise QAEngineError(
                "It was not possible to access the Q&A service."
            ) from error
        except(KeyError, IndexError, TypeError, ValueError) as error:
            raise QAEngineError(
                "The service returned a response in an unexpected format."
            ) from error

    @staticmethod
    def clean_answer(content):
        """Remove reasoning and common Markdown artifacts from the final answer."""
        cleaned = re.sub(
            r"<think>.*?</think>",
            "",
            content,
            flags=re.IGNORECASE | re.DOTALL,
        ).strip()
        cleaned = cleaned.replace("**", "").replace("__", "")
        cleaned = re.sub(r"(?m)^\s*[-*]\s+", "• ", cleaned)
        cleaned = re.sub(r"(?m)^\s*#{1,6}\s*", "", cleaned)
        cleaned = re.sub(r"\n{3,}", "\n\n", cleaned)
        return cleaned.strip()
