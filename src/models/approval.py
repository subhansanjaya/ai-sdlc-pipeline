from pydantic import BaseModel

class Approval(BaseModel):
    stage: str
    approved: bool
    approved_by: str
    comments: str = ""