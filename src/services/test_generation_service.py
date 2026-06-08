from src.agents.test_agent import (
    TestAgent,
)

from src.providers.factory import (
    get_provider,
)

from src.models.spec import (
    FeatureSpecification,
)

from src.models.plan import (
    ImplementationPlan,
)

def generate_tests(
    spec: FeatureSpecification,
    plan: ImplementationPlan,
) -> str:

    provider = get_provider()

    agent = TestAgent(
        provider
    )

    return agent.generate_tests(
        spec,
        plan,
    )