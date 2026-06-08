import ollama
from src.providers.base import LLMProvider

class OllamaProvider(LLMProvider):

    def generate(self, prompt: str) -> str:

        response = ollama.chat(
            model="llama3.1",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return str(
            response["message"]["content"]
        )