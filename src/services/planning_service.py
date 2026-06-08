from src.agents.planner_agent import (
    PlannerAgent,
)

from src.providers.factory import (
    get_provider,
)

from src.models.spec import FeatureSpecification
from src.models.plan import ImplementationPlan

def create_plan(
    spec: FeatureSpecification,
) -> ImplementationPlan:

    provider = get_provider()

    planner = PlannerAgent(
        provider
    )

    return planner.generate_plan(
        spec
    )