"""Civic AI agents for East Africa."""
import os
from typing import Optional


class RightsAgent:
    """Constitutional rights Q&A in English and Kiswahili."""
    RIGHTS = {
        "en": {
            "land": "Article 40: Every person has the right to acquire and own property.",
            "education": "Article 43: Every person has the right to free and compulsory basic education.",
            "water": "Article 43: Every person has the right to clean and safe water.",
            "health": "Article 43: Every person has the right to healthcare services.",
            "labour": "Article 41: Every person has the right to fair labour practices.",
        },
        "sw": {
            "ardhi": "Kifungu 40: Kila mtu ana haki ya kupata na kumiliki mali.",
            "elimu": "Kifungu 43: Kila mtu ana haki ya elimu ya msingi bure na ya lazima.",
            "maji": "Kifungu 43: Kila mtu ana haki ya maji safi na salama.",
            "afya": "Kifungu 43: Kila mtu ana haki ya huduma za afya.",
            "kazi": "Kifungu 41: Kila mtu ana haki ya mazoea ya haki ya kazi.",
        },
    }

    def __init__(self, language: str = "en"):
        self.language = language.lower()[:2]

    def ask(self, question: str) -> str:
        rights = self.RIGHTS.get(self.language, self.RIGHTS["en"])
        q_lower = question.lower()
        for key, text in rights.items():
            if key in q_lower:
                return f"[Constitution of Kenya 2010]\n{text}"
        keys = ", ".join(rights.keys())
        return f"Right not found. Available topics: {keys}"


class DroughtAgent:
    """NDMA drought status for Kenya counties."""
    import hashlib as _hashlib

    PHASES = {1: "Minimal", 2: "Stressed", 3: "Crisis", 4: "Emergency", 5: "Famine"}

    def get_status(self, county: str) -> dict:
        import hashlib
        h = int(hashlib.md5(county.encode()).hexdigest()[:4], 16) % 4 + 1
        return {
            "county": county,
            "phase": h,
            "phase_label": self.PHASES[h],
            "source": "NDMA Kenya (sandbox)",
        }


class BudgetAgent:
    """County budget analysis agent."""
    def analyse(self, county: str, data_path: Optional[str] = None) -> str:
        try:
            import pandas as pd
            from .data import KenyaBudgetData
            df = KenyaBudgetData.load()
            matches = df[df.apply(lambda r: county.lower() in " ".join(r.astype(str).str.lower()), axis=1)]
            if matches.empty:
                return f"No budget data for {county}"
            return matches.to_string(index=False)
        except FileNotFoundError as e:
            return str(e)
