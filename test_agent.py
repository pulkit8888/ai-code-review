from app.agents.base_agent import BaseAgent


class TestAgent(BaseAgent):

    def build_prompt(self, code_diff):

        return f"""
        Explain this code:

        {code_diff}
        """


agent = TestAgent(
    "test-agent"
)


result = agent.review(
    """
    def add(a,b):
        return a+b
    """
)


print(result)