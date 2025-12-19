from abc import ABC, abstractmethod
from typing import Dict, Any, Optional


class CognitiveEngine(ABC):
    """
    Abstract cognitive engine.
    One instance per experiment run.
    """

    @abstractmethod
    def process(
        self,
        text: str,
        task: str,
        context: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Process text according to a task and optional context.

        Returns a dict with:
          - text: free-form explanation
          - data: structured result
          - meta (optional): additional notes
        """
        pass
