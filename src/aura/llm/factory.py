import os

from aura.llm.base import CognitiveEngine
from aura.llm.mock_provider import MockCognitiveEngine
from aura.llm.openai_provider import OpenAICognitiveEngine


def create_cognitive_engine() -> CognitiveEngine:
    """
    Decide which cognitive engine to use based on environment.
    """

    api_key = os.getenv("OPENAI_API_KEY")

    if api_key:
        print("[AURA] Using OpenAI cognitive engine (OPENAI_API_KEY found)")
        return OpenAICognitiveEngine(api_key=api_key)

    print("[AURA] Using mock cognitive engine (no OPENAI_API_KEY key found)")
    return MockCognitiveEngine()
