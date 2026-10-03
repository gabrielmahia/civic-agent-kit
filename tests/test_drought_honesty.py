"""Honesty tests for the drought agent and the embedded data. The previous suite only checked that files parse and the package imports,
so this package could be green while serving values labelled as NDMA data that were derived from a hash of the county name."""
import importlib.util
import pathlib

SRC = pathlib.Path(__file__).resolve().parents[1] / "src" / "civic_agent_kit"


def _agents():
    spec = importlib.util.spec_from_file_location("agents_under_test", SRC / "agents.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_drought_status_is_labelled_synthetic():
    r = _agents().DroughtAgent().get_status("Turkana")
    assert r["is_synthetic"] is True and "NOT NDMA" in r["source"]


def test_drought_agent_docstring_does_not_claim_real_data():
    doc = _agents().DroughtAgent.__doc__
    assert "DEMO" in doc and "NOT NDMA" in doc


def test_mcp_instructions_disclose_that_embedded_data_is_unsourced():
    assert "sources and as-of dates are not recorded" in (SRC / "server.py").read_text()
