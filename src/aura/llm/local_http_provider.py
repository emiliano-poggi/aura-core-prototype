import requests
from typing import Dict, Any, Optional
from aura.llm.base import CognitiveEngine


class LocalHttpCognitiveEngine(CognitiveEngine):
    """
    Cognitive engine backed by a local HTTP LLM service.
    """

    def __init__(self, endpoint: str):
        self.endpoint = endpoint.rstrip("/")

    def process(
        self,
        text: str,
        task: str,
        context: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:

        # ---- compose prompt explicitly ----
        composed_prompt = (
            f"Task:\n{task}\n\n"
            f"Context:\n{context}\n\n"
            f"Text:\n{text}\n\n"
            "Respond with:\n"
            "- A concise explanation\n"
            "- No markdown\n"
        )

        payload = {
            "model": "mistral",
            "prompt": composed_prompt,
            "stream": False,
        }

        try:
            response = requests.post(self.endpoint, json=payload, timeout=30)
            response.raise_for_status()
        except Exception as e:
            return {
                "text": f"Local LLM error: {e}",
                "data": {},
                "meta": {
                    "engine": "local",
                    "error": True,
                },
            }

        data = response.json()

        return {
            "text": data.get("text", ""),
            "data": data.get("data", {}),
            "meta": {
                "engine": "local",
                "endpoint": self.endpoint,
            },
        }
