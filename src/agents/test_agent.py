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

from src.prompts.prompt_loader import (
    load_test_prompt,
)

from src.services.audit_service import (
    write_audit_record,
)


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

        prompt_config = load_test_prompt()

        test_prompt = prompt_config[
            "template"
        ]

        test_version = prompt_config[
            "version"
        ]

        prompt = test_prompt.format(
            acceptance_criteria="\n".join(
                spec.acceptance_criteria
            ),
            implementation_plan=plan.model_dump_json(
                indent=2
            ),
        )

        response = self.provider.generate(
            prompt
        )

        tests = self._extract_code(
            response
        )

        write_audit_record(
            "tests_generated",
            {
                "prompt_version":
                    test_version,
                "feature_objective":
                    spec.feature_objective,
                "test_length":
                    len(tests),
                "acceptance_criteria_count":
                    len(
                        spec.acceptance_criteria
                    ),
            },
        )

        return tests

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