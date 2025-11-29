import re
from typing import Dict


class ClauseExtractor:
    """
    Very simple regex/keyword-based clause extractor.
    In a real system, this can be upgraded to an LLM or classifier-based layer.
    """

    def extract(self, text: str) -> Dict[str, str]:
        return {
            "pricing": self._find_pricing_clause(text),
            "rebate": self._find_rebate_clause(text),
            "termination": self._find_termination_clause(text),
            "sla": self._find_sla_clause(text),
        }

    def _find_pricing_clause(self, text: str) -> str:
        return self._find_section(text, ["price", "pricing", "fees"])

    def _find_rebate_clause(self, text: str) -> str:
        return self._find_section(text, ["rebate", "discount", "chargeback"])

    def _find_termination_clause(self, text: str) -> str:
        return self._find_section(text, ["termination", "term", "duration"])

    def _find_sla_clause(self, text: str) -> str:
        return self._find_section(text, ["service level", "SLA", "availability"])

    def _find_section(self, text: str, keywords):
        pattern = r"(.{0,300}(" + "|".join(keywords) + r").{0,800})"
        match = re.search(pattern, text, flags=re.IGNORECASE | re.DOTALL)
        return match.group(0).strip() if match else ""
