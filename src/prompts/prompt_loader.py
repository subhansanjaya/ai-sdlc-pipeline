from typing import Any

import yaml

from src.prompts.registry import (
    PROMPTS,
)


def _load_prompt(
    config_key: str,
) -> dict[str, Any]:

    with open(
        "config.yaml"
    ) as file:

        config = yaml.safe_load(
            file
        )

    version = config[
        config_key
    ]

    return PROMPTS[
        version
    ]


def load_planner_prompt() -> dict[str, Any]:

    return _load_prompt(
        "planner_prompt_version"
    )


def load_implementation_prompt() -> dict[str, Any]:

    return _load_prompt(
        "implementation_prompt_version"
    )


def load_test_prompt() -> dict[str, Any]:

    return _load_prompt(
        "test_prompt_version"
    )