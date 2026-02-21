from dataclasses import dataclass
from typing import List

@dataclass
class UserContext:
    user_id: str
    user_role: str  # beginner, expert, recruiter

@dataclass
class AgentResponse:
    summary: str
    key_points: List[str]
    confidence: float