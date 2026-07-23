from abc import ABC, abstractmethod

from app.ai.gemini_client import GeminiClient


class BaseAgent(ABC):

    def __init__(self, name: str):
        self.name = name
        self.llm = GeminiClient()


    @abstractmethod
    def build_prompt(self, code_diff: str) -> str:
        pass


    def review(self, code_diff: str):

        prompt = self.build_prompt(
            code_diff
        )

        response = self.llm.generate(
            prompt
        )

        return response