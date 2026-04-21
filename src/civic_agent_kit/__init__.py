"""
CivicAgentKit — Python SDK for East African civic AI.
"""

__version__ = "0.1.0"
__author__  = "Gabriel Mahia"
__email__   = "contact@aikungfu.dev"

from .data import KenyaBudgetData, KenyaParliamentData, KenyaSACCOData
from .agents import BudgetAgent, RightsAgent, DroughtAgent
from .utils import KenyaCounties, KiswahiliTranslator

__all__ = [
    "KenyaBudgetData",
    "KenyaParliamentData",
    "KenyaSACCOData",
    "BudgetAgent",
    "RightsAgent",
    "DroughtAgent",
    "KenyaCounties",
    "KiswahiliTranslator",
]
