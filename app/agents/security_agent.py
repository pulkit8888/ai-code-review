from app.agents.base_agent import BaseAgent
from app.prompts.security_prompt import SECURITY_REVIEW_PROMPT


class SecurityAgent(BaseAgent):

    def __init__(self):
        super().__init__(
            "security-agent"
        )


    def build_prompt(
        self,
        code_diff: str
    ):

        return SECURITY_REVIEW_PROMPT.format(
            code_diff=code_diff
        )