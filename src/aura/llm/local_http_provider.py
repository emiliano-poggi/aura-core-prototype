import requests, json, re
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

        # ---- AI Prompt ----
        composed_prompt = (
            f"Task:\n{task}\n\n"
            f"Context:\n{context}\n\n"
            f"Text:\n{text}\n\n"
            "Return your answer in TWO parts exactly as follows.\n\n"
            "AI_EXPLANATION:\n"
            "<concise explanation in plain text>\n\n"
            "AI_DATA:\n"
            "<a single-line JSON object with only the required keys>\n\n"
            "Rules:\n"
            "- The JSON must be valid.\n"
            "- Use arrays of strings.\n"
            "- If nothing applies, return empty arrays.\n"
        )

        payload = {
            "model": "mistral",
            "prompt": composed_prompt,
            "stream": False,
        }

        # ---- Request ----
        try:
            response = requests.post(self.endpoint, json=payload, timeout=60)
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


        # ---- Extractor ----
        data = response.json()
        raw_text = data.get("response", "")
        raw_data_block = None
        structured = {}
        match_data = re.search(r"AI_DATA:\s*(\{.*\})", raw_text, re.DOTALL)

        if match_data:
            try:
                raw_data_block = match.group(1)
                structured = json.loads(match.group(1))
            except json.JSONDecodeError:
                structured = {}

        themes = structured.get("themes", [])
        entities = structured.get("entities", [])
        events = structured.get("events", [])

        if not isinstance(themes, list):
            themes = []
        if not isinstance(entities, list):
            entities = []
        if not isinstance(events, list):
            events = []

        # ---- Cognitive response ----
        return {
            "text": raw_text,
            "data": {
                "themes": themes,
                "entities": entities,
                "events": events,
            },
            "meta": {
                "engine": "local",
                "endpoint": self.endpoint,
                "raw_data": raw_data_block
            },
        }
