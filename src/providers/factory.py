import yaml

from src.providers.openai_provider import (
    OpenAIProvider,
)

from src.providers.ollama_provider import (
    OllamaProvider,
)

from src.providers.base import LLMProvider

def get_provider() -> LLMProvider:

    config = yaml.safe_load(
        open("config.yaml")
    )

    provider = config["provider"]

    if provider == "openai":
        return OpenAIProvider()

    return OllamaProvider()