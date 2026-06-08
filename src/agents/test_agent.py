import re

from src.models.plan import ImplementationPlan
from src.models.spec import FeatureSpecification
from src.providers.base import LLMProvider

class TestAgent:

    def __init__(
        self,
        provider: LLMProvider,
    ) -> None:
        self.provider = provider

    def generate_tests(
        self,
        spec: FeatureSpecification,
        plan: ImplementationPlan,
    ) -> str:

        prompt = f"""
You are a senior QA engineer.

Generate pytest tests.

Requirements:

- Generate unit tests
- Generate integration tests
- Generate acceptance tests
- Map tests to acceptance criteria
- Return Python code only

Acceptance Criteria:
{spec.acceptance_criteria}

Implementation Plan:
{plan.model_dump_json(indent=2)}
"""

        response = self.provider.generate(
            prompt
        )

        return self._extract_code(
            response
        )

    def _extract_code(
        self,
        text: str,
    ) -> str:

        match = re.search(
            r"```(?:python)?(.*?)```",
            text,
            re.DOTALL,
        )

        if match:
            return match.group(1).strip()

        return text.strip()