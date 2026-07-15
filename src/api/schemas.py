from pydantic import BaseModel

class PipelineRequest(BaseModel):
    spec: str
    provider: str = "openai"
    model: str = "gpt-4.1-mini"
    path: str

class PipelineResponse(BaseModel):
    thread_id: str
    status: str