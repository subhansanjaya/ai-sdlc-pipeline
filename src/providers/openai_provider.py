import os

from openai import OpenAI
from src.providers.base import LLMProvider
from dotenv import load_dotenv

load_dotenv()

class OpenAIProvider(LLMProvider):

    def __init__(self) -> None:
        self.client = OpenAI(
            api_key=os.getenv("OPENAI_API_KEY")
        )

    def generate(self, prompt: str) -> str:

        response = self.client.responses.create(
            model=os.getenv(
                "OPENAI_MODEL",
                "gpt-4.1-mini"
            ),
            input=prompt
        )

        return response.output_text