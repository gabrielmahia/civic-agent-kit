"""
CivicAgentKit — Python SDK for East African civic AI.
"""

__version__ = "0.1.0"
__author__  = "Gabriel Mahia"
__email__   = "contact@aikungfu.dev"

from .agents import BudgetAgent, DroughtAgent, RightsAgent
from .data import KenyaBudgetData, KenyaParliamentData, KenyaSACCOData
from .utils import KenyaCounties, KiswahiliTranslator

__all__ = [
    "BudgetAgent",
    "DroughtAgent",
    "KenyaBudgetData",
    "KenyaCounties",
    "KenyaParliamentData",
    "KenyaSACCOData",
    "KiswahiliTranslator",
    "RightsAgent",
]
