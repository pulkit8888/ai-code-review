from pydantic import BaseModel


class ReviewIssue(BaseModel):
    title: str
    severity: str
    line: int
    description: str
    recommendation: str


class AgentReview(BaseModel):
    agent: str
    issues: list[ReviewIssue]