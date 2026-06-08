from src.prompts.planner_v1 import (
    PLANNER_PROMPT,
)

from src.prompts.implementation_v1 import (
    IMPLEMENTATION_PROMPT,
)

from src.prompts.tests_v1 import (
    TEST_PROMPT,
)


PROMPTS = {
    "planner_v1": {
        "template": PLANNER_PROMPT,
        "version": "planner_v1",
    },
    "implementation_v1": {
        "template": IMPLEMENTATION_PROMPT,
        "version": "implementation_v1",
    },
    "tests_v1": {
        "template": TEST_PROMPT,
        "version": "tests_v1",
    },
}