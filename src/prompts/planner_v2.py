from langchain_core.prompts import PromptTemplate

PLANNER_PROMPT_VERSION = "planner_v2"

PLANNER_PROMPT = PromptTemplate(
    template="""
You are a senior software architect.

Return ONLY valid JSON.

Do not return markdown.
Do not return explanations.

Return EXACTLY this structure:

{{
    "implementation_tasks": [],
    "technical_design_summary": "",
    "impacted_modules": [],
    "risks": [],
    "test_strategy": []
}}

Feature Objective:
{feature_objective}

User Story:
{user_story}

Business Rules:
{business_rules}

Acceptance Criteria:
{acceptance_criteria}

Non Functional Requirements:
{non_functional_requirements}
""",
    input_variables=[
        "feature_objective",
        "user_story",
        "business_rules",
        "acceptance_criteria",
        "non_functional_requirements",
    ],
)