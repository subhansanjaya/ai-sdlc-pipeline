import yaml

from src.prompts.registry import (
    PROMPTS,
)


def _load_prompt(
    config_key: str,
):

    config = yaml.safe_load(
        open(
            "config.yaml"
        )
    )

    version = config[
        config_key
    ]

    return PROMPTS[
        version
    ]


def load_planner_prompt():

    return _load_prompt(
        "planner_prompt_version"
    )


def load_implementation_prompt():

    return _load_prompt(
        "implementation_prompt_version"
    )


def load_test_prompt():

    return _load_prompt(
        "test_prompt_version"
    )