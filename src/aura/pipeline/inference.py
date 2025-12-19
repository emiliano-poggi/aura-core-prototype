from typing import Dict, Any
from aura.llm.base import CognitiveEngine


def inference_analysis(
    engine: CognitiveEngine,
    text: str,
    interpretation_mode: str,
    experiment_name: str,
) -> Dict[str, Any]:
    """
    Minimal inference analysis using the cognitive engine (mock).
    Focus: entities and events only.
    """

    result = engine.process(
        text=text,
        task="inference: extract implied entities and events",
        context={
            "experiment": experiment_name,
            "mode": interpretation_mode,
        },
    )

    data = result.get("data", {})
    entities = data.get("entities", [])
    events = data.get("events", [])

    if not isinstance(entities, list):
        entities = []
    if not isinstance(events, list):
        events = []

    return {
        "explanation": result.get("text", ""),
        "entities": entities,
        "events": events,
        "meta": result.get("meta", {}),
    }
