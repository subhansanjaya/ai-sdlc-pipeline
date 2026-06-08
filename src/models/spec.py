from typing import List
from pydantic import BaseModel

class FeatureSpecification(BaseModel):
    feature_objective: str
    user_story: str
    business_rules: List[str]
    acceptance_criteria: List[str]
    non_functional_requirements: List[str]
    out_of_scope_items: List[str] = []