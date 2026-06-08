from langchain_core.prompts import PromptTemplate

TEST_PROMPT_VERSION = "tests_v1"

TEST_PROMPT = PromptTemplate(
    template="""
You are a senior QA engineer.

Generate pytest tests.

Requirements:

- Generate unit tests
- Generate integration tests
- Generate acceptance tests
- Map tests to acceptance criteria
- Return Python code only

Acceptance Criteria:
{acceptance_criteria}

Implementation Plan:
{implementation_plan}
""",
    input_variables=[
        "acceptance_criteria",
        "implementation_plan",
    ],
)