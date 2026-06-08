from typing import TypedDict

from src.models.spec import (
    FeatureSpecification,
)

from src.models.plan import (
    ImplementationPlan,
)

class PipelineState(
    TypedDict
):
    spec: FeatureSpecification
    plan: ImplementationPlan | None
    code: str | None
    tests: str | None