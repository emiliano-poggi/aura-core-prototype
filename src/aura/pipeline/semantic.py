from typing import Dict, Any
from aura.llm.base import CognitiveEngine


def semantic_analysis(
    engine: CognitiveEngine,
    text: str,
    interpretation_mode: str,
    experiment_name: str ) -> Dict[str, Any]:
    """
    Minimal semantic analysis using the cognitive engine.
    Focus: themes only.
    """

    result = engine.process(
        text=text,
        task="semantic: identify dominant themes",
        context={
            "experiment": experiment_name,
            "mode": interpretation_mode,
        },
    )

    # Enforce minimal expected shape
    themes = result.get("data", {}).get("themes", [])
    if not isinstance(themes, list):
        themes = []

    return {
        "explanation": result.get("text", ""),
        "themes": themes,
        "meta": result.get("meta", {}),
    }
