from typing import List
from pydantic import BaseModel

class ImplementationPlan(BaseModel):

    implementation_tasks: List[str]
    technical_design_summary: str
    impacted_modules: List[str]
    risks: List[str]
    test_strategy: List[str]