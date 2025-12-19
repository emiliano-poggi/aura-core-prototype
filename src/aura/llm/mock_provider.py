from typing import Dict, Any, Optional
from aura.llm.base import CognitiveEngine


class MockCognitiveEngine(CognitiveEngine):
    """
    Deterministic mock implementation of the cognitive engine.
    Does NOT use AI or external services.
    """

    def process(
        self,
        text: str,
        task: str,
        context: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:

        text_length = len(text)
        word_count = len(text.split())

        if task.startswith("semantic:"):
                # Deterministic, fake themes
                themes = []
                if word_count > 0:
                    themes = ["memory", "fragmentation"]
                return {
                "text": (
                    "This mock semantic analysis identifies recurring "
                    "abstract concepts based on simple heuristics."
                ),
                "data": {
                    "themes": themes,
                },
                "meta": {
                    "engine": "mock",
                    "deterministic": True,
                },
            }

        return {
            "text": (
                "This is a mock cognitive response. "
                "No real inference has been performed. "
                f"The task was: '{task}'."
            ),
            "data": {
                "task": task,
                "text_length": text_length,
                "word_count": word_count,
                "context_received": bool(context),
            },
            "meta": {
                "engine": "mock",
                "deterministic": True,
            },
        }
