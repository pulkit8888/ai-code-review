from google import genai
from google.genai import types

from app.utils.config import settings


class GeminiClient:
    """
    Wrapper around Gemini API.

    Responsibilities:
    - Initialize Gemini client
    - Send prompts
    - Return model responses
    """


    def __init__(self):
        self.client = genai.Client(
            api_key=settings.GEMINI_API_KEY
        )

        self.model = settings.GEMINI_MODEL


    def generate(
        self,
        prompt: str,
    ) -> str:
        """
        Send prompt to Gemini and return response text.
        """

        try:
            response = self.client.models.generate_content(
                model=self.model,
                contents=prompt,
                config=types.GenerateContentConfig(
                    temperature=0.2
                )
            )

            return response.text

        except Exception as e:
            raise RuntimeError(
                f"Gemini API failed: {str(e)}"
            )