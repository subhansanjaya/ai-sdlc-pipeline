from pydantic import BaseModel

class GeneratedCode(BaseModel):
    filename: str
    content: str