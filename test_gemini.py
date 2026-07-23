from app.ai.gemini_client import GeminiClient


client = GeminiClient()


response = client.generate(
    """
    Return only JSON.

    {
        "message": "hello"
    }
    """
)


print(response)