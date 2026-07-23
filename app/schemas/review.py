from pydantic import BaseModel
from typing import List


class Finding(BaseModel):
    severity: str
    category: str
    message: str
    suggestion: str
    line: int | None = None


class AgentResponse(BaseModel):
    agent: str
    findings: List[Finding]