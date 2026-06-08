from pydantic import BaseModel

class WorkflowState(BaseModel):
    spec_path: str
    spec_content: str = ""
    plan: str = ""
    implementation_complete: bool = False