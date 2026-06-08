from langchain_core.prompts import PromptTemplate

IMPLEMENTATION_PROMPT_VERSION = "implementation_v1"

IMPLEMENTATION_PROMPT = PromptTemplate(
    template="""
You are a senior software engineer.

Generate implementation code only.

Rules:

- Generate executable Python code
- Do not generate tests
- Do not generate markdown
- Do not generate explanations
- Do not generate comments unless necessary
- Implement only what is required by the specification
- Return code only

Feature Objective:
{feature_objective}

Business Rules:
{business_rules}

Acceptance Criteria:
{acceptance_criteria}

Implementation Plan:
{implementation_plan}
""",
    input_variables=[
        "feature_objective",
        "business_rules",
        "acceptance_criteria",
        "implementation_plan",
    ],
)