import os
from typing import Dict, Any, Optional

from aura.llm.base import CognitiveEngine


class OpenAICognitiveEngine(CognitiveEngine):
    """
    Minimal OpenAI-backed cognitive engine.
    """

    def __init__(self, api_key: str):
        self.api_key = api_key

    def process(
        self,
        text: str,
        task: str,
        context: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        # Minimal, synchronous call
        # NOTE: deliberately simple, no tuning, no streaming

        from openai import OpenAI  # imported here to avoid hard dependency at import time

        client = OpenAI(api_key=self.api_key)

        prompt = (
            f"Task: {task}\n\n"
            f"Context: {context}\n\n"
            f"Text:\n{text}\n\n"
            "Return:\n"
            "1) A brief explanation in plain text\n"
            "2) A JSON object with the requested structured data"
        )

        response = client.responses.create(
            model="gpt-4.1-mini",
            input=prompt,
        )

        # Very defensive parsing (v0.1)
        output_text = response.output_text

        return {
            "text": output_text,
            "data": {},
            "meta": {
                "engine": "openai",
                "model": "gpt-4.1-mini",
            },
        }
