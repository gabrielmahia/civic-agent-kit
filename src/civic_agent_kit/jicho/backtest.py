from __future__ import annotations

from dataclasses import dataclass

from .core import CaseRecord, coverage_critic, due_process_red_team


@dataclass(frozen=True)
class BacktestResult:
    case_id: str
    predicted: str
    expected: str | None
    leading_score: float
    null_score: float
    coverage_score: float
    coverage_gaps: tuple[str, ...]
    passed: bool


def run_case(case: CaseRecord, leading_id: str = "leading", null_id: str = "null") -> BacktestResult:
    leading = case.hypothesis_score(leading_id)
    null = case.hypothesis_score(null_id)
    predicted = "investigate" if leading > null + 0.15 else "do_not_escalate"
    expected = case.expected_outcome
    return BacktestResult(
        case_id=case.id,
        predicted=predicted,
        expected=expected,
        leading_score=round(leading, 3),
        null_score=round(null, 3),
        coverage_score=round(case.coverage.score(), 3),
        coverage_gaps=tuple(case.coverage.missing()),
        passed=(expected is None or predicted == expected),
    )


def diagnostic(case: CaseRecord) -> dict[str, object]:
    return {
        "coverage_critic": coverage_critic(case.coverage),
        "due_process_red_team": due_process_red_team(case, "leading"),
    }
