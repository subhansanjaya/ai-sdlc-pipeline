import re

from src.models.plan import (
    ImplementationPlan,
)

from src.models.spec import (
    FeatureSpecification,
)

from src.providers.base import (
    LLMProvider,
)

class ImplementationAgent:

    def __init__(
        self,
        provider: LLMProvider,
    ):
        self.provider = provider

    def generate_code(
        self,
        spec: FeatureSpecification,
        plan: ImplementationPlan,
    ) -> str:

        #         prompt = f"""
        # You are a senior software engineer.

        # Generate ONLY Python code.

        # Feature Objective:
        # {spec.feature_objective}

        # Business Rules:
        # {spec.business_rules}

        # Acceptance Criteria:
        # {spec.acceptance_criteria}

        # Implementation Plan:
        # {plan.model_dump_json(indent=2)}

        # Return code only.
        # """

        prompt = f"""
        You are implementing a feature.

        Generate ONE Python module only.

        Requirements:

        - Generate implementation code only
        - Do NOT generate tests
        - Do NOT generate explanations
        - Do NOT generate markdown
        - Do NOT generate database code
        - Do NOT generate APIs
        - Do NOT generate classes unless required
        - Return only executable Python code

        Feature Objective:
        {spec.feature_objective}

        Business Rules:
        {spec.business_rules}

        Acceptance Criteria:
        {spec.acceptance_criteria}

        The generated code must directly implement the acceptance criteria.
        """

        response = self.provider.generate(
            prompt
        )

        code = self._extract_code(
            response
        )

        return code

    def _extract_code(
        self,
        text: str,
    ) -> str:

        match = re.search(
            r"```python(.*?)```",
            text,
            re.DOTALL,
        )

        if match:
            return match.group(1).strip()

        return text.strip()