"""Smoke tests for civic-agent-kit."""
from civic_agent_kit import RightsAgent, DroughtAgent, KenyaCounties, KiswahiliTranslator

def test_rights_en():
    a = RightsAgent(language="en")
    r = a.ask("What is my right to education?")
    assert "Article" in r or "not found" in r

def test_rights_sw():
    a = RightsAgent(language="sw")
    r = a.ask("Haki yangu ya maji ni nini?")
    assert "Kifungu" in r or "haipatikani" in r or "not found" in r

def test_drought_agent():
    d = DroughtAgent()
    s = d.get_status("Nairobi")
    assert "phase" in s
    assert 1 <= s["phase"] <= 5

def test_counties():
    assert "Nairobi" in KenyaCounties.all
    assert len(KenyaCounties.all) == 47
    assert KenyaCounties.is_valid("Turkana")

def test_translator():
    r = KiswahiliTranslator.translate("education budget")
    assert "elimu" in r or "bajeti" in r
