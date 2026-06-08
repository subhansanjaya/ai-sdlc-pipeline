import json
import logging
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

class PlannerAgent:

    def __init__(
        self,
        provider: LLMProvider,
    ):
        self.provider = provider

    def generate_plan(
        self,
        spec: FeatureSpecification,
    ) -> ImplementationPlan:

        #         prompt = f"""
        # You are a software architect.

        # Generate JSON only.

        # Return:

        # {{
        #   "implementation_tasks": [],
        #   "technical_design_summary": "",
        #   "impacted_modules": [],
        #   "risks": [],
        #   "test_strategy": []
        # }}

        # Feature Objective:
        # {spec.feature_objective}

        # User Story:
        # {spec.user_story}

        # Business Rules:
        # {spec.business_rules}

        # Acceptance Criteria:
        # {spec.acceptance_criteria}

        # Non Functional Requirements:
        # {spec.non_functional_requirements}
        # """

        prompt = f"""
        You are a software architect.

        Return ONLY valid JSON.

        Do not return markdown.
        Do not return explanations.
        Do not return feature summaries.
        Do not return user stories.
        Do not return business rules.
        Do not return acceptance criteria.

        Return EXACTLY this JSON structure:

        {{
        "implementation_tasks": [
            "task 1"
        ],
        "technical_design_summary": "summary",
        "impacted_modules": [
            "module"
        ],
        "risks": [
            "risk"
        ],
        "test_strategy": [
            "test strategy"
        ]
        }}

        Feature Objective:
        {spec.feature_objective}

        User Story:
        {spec.user_story}

        Business Rules:
        {spec.business_rules}

        Acceptance Criteria:
        {spec.acceptance_criteria}

        Non Functional Requirements:
        {spec.non_functional_requirements}
        """

        response = self.provider.generate(
            prompt
        )

        logging.info("Plan generated")

        json_match = re.search(
            r"\{.*\}",
            response,
            re.DOTALL,
        )

        if not json_match:
            raise ValueError(
                "No JSON found in model response"
            )

        data = json.loads(
            json_match.group(0)
        )


        required_fields = [
            "implementation_tasks",
            "technical_design_summary",
            "impacted_modules",
            "risks",
            "test_strategy",
        ]

        missing = [
            field
            for field in required_fields
            if field not in data
        ]

        if missing:
            raise ValueError(
                f"Planner response missing required fields: {missing}"
            )

        # print("\n===== PLAN JSON =====")
        # print(json.dumps(data, indent=2))
        # print("=====================\n")

        return ImplementationPlan(
            **data
        )
    
    