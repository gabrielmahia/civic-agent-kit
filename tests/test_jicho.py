from civic_agent_kit.jicho.backtest import run_case
from civic_agent_kit.jicho.fixtures import all_cases, false_allegation, ghost_road


def test_mock_backtests_match_expected():
    results = [run_case(c) for c in all_cases()]
    assert all(r.passed for r in results), results


def test_false_allegation_does_not_escalate():
    assert run_case(false_allegation()).predicted == "do_not_escalate"


def test_ghost_road_escalates():
    assert run_case(ghost_road()).predicted == "investigate"


def test_publication_guard_rejects_low_state():
    ok, reasons = false_allegation().publication_ready("viral")
    assert not ok
    assert any("publishable" in r for r in reasons)
