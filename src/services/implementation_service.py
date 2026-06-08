from src.agents.implementation_agent import (
    ImplementationAgent,
)

from src.providers.factory import (
    get_provider,
)

from src.models.spec import FeatureSpecification
from src.models.plan import ImplementationPlan

def generate_implementation(
    spec: FeatureSpecification,
    plan: ImplementationPlan,
) -> str:

    provider = get_provider()

    agent = ImplementationAgent(
        provider
    )

    return agent.generate_code(
        spec,
        plan,
    )