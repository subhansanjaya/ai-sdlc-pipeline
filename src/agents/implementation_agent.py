import re

from src.prompts.prompt_loader import (
    load_implementation_prompt,
)

from src.models.plan import (
    ImplementationPlan,
)

from src.models.spec import (
    FeatureSpecification,
)

from src.providers.base import (
    LLMProvider,
)

from src.services.audit_service import (
    write_audit_record,
)


class ImplementationAgent:

    def __init__(
        self,
        provider: LLMProvider,
    ) -> None:
        self.provider = provider

    def generate_code(
        self,
        spec: FeatureSpecification,
        plan: ImplementationPlan,
    ) -> str:
        
        prompt_config = load_implementation_prompt()

        implementation_prompt = prompt_config[
            "template"
        ]

        implementation_version = prompt_config[
            "version"
        ]

        prompt = implementation_prompt.format(
            feature_objective=spec.feature_objective,
            business_rules="\n".join(
                spec.business_rules
            ),
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

        code = self._extract_code(
            response
        )

        write_audit_record(
            "implementation_generated",
            {
                "prompt_version":
                    implementation_version,
                "feature_objective":
                    spec.feature_objective,
                "code_length":
                    len(code),
                "implementation_tasks":
                    len(
                        plan.implementation_tasks
                    ),
            },
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