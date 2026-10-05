from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class EvidenceState(str, Enum):
    LEAD = "lead"
    CORROBORATED_ALLEGATION = "corroborated_allegation"
    DOCUMENTED_DISCREPANCY = "documented_discrepancy"
    INVESTIGATIVE_FINDING = "investigative_finding"
    OFFICIAL_FINDING = "official_finding"
    SANCTION_OR_DEBARMENT = "sanction_or_debarment"
    CONVICTION = "conviction"
    CLEARED_REVERSED_CORRECTED = "cleared_reversed_corrected"


@dataclass(frozen=True)
class Source:
    id: str
    source_type: str
    locator: str
    independence_family: str
    reliability: float = 0.5


@dataclass(frozen=True)
class Claim:
    id: str
    subject: str
    predicate: str
    object_value: str
    status: EvidenceState
    source_ids: tuple[str, ...]
    direct: bool = True
    confidence: float = 0.5
    coverage_confidence: float = 0.0
    supports: tuple[str, ...] = ()
    contradicts: tuple[str, ...] = ()


@dataclass(frozen=True)
class Hypothesis:
    id: str
    label: str
    predicted_claim_ids: tuple[str, ...] = ()
    falsifier_claim_ids: tuple[str, ...] = ()


COVERAGE_DIMENSIONS = (
    "identity", "relationships", "geography", "language", "time", "format",
    "source_class", "role", "asset_class", "negative_space",
)


@dataclass
class CoverageAudit:
    checked: dict[str, bool] = field(default_factory=dict)

    def score(self) -> float:
        return sum(bool(self.checked.get(k, False)) for k in COVERAGE_DIMENSIONS) / len(COVERAGE_DIMENSIONS)

    def missing(self) -> list[str]:
        return [k for k in COVERAGE_DIMENSIONS if not self.checked.get(k, False)]


@dataclass
class CaseRecord:
    id: str
    title: str
    sources: dict[str, Source]
    claims: dict[str, Claim]
    hypotheses: dict[str, Hypothesis]
    coverage: CoverageAudit
    expected_outcome: str | None = None

    def independent_source_families(self, claim: Claim) -> set[str]:
        return {self.sources[sid].independence_family for sid in claim.source_ids if sid in self.sources}

    def publication_ready(self, claim_id: str) -> tuple[bool, list[str]]:
        claim = self.claims[claim_id]
        reasons: list[str] = []
        if claim.status in {EvidenceState.LEAD, EvidenceState.CORROBORATED_ALLEGATION}:
            reasons.append("claim has not reached a publishable finding state")
        if len(self.independent_source_families(claim)) < 1:
            reasons.append("no independently traceable source family")
        if claim.confidence < 0.75:
            reasons.append("answer confidence below 0.75")
        if claim.coverage_confidence < 0.60:
            reasons.append("coverage confidence below 0.60")
        return (not reasons, reasons)

    def hypothesis_score(self, hypothesis_id: str) -> float:
        h = self.hypotheses[hypothesis_id]
        score = 0.0
        weight = 0.0
        for cid in h.predicted_claim_ids:
            if cid in self.claims:
                score += self.claims[cid].confidence
                weight += 1
        for cid in h.falsifier_claim_ids:
            if cid in self.claims:
                score -= self.claims[cid].confidence
                weight += 1
        return 0.0 if weight == 0 else score / weight


def coverage_critic(audit: CoverageAudit) -> list[str]:
    prompts = {
        "identity": "Search aliases, former names, transliterations, and near-identical entities.",
        "relationships": "Search relatives, directors, lawyers, agents, trustees, and recurring intermediaries.",
        "geography": "Expand to every jurisdiction touched by people, entities, payments, or assets.",
        "language": "Repeat retrieval in relevant local languages and scripts.",
        "time": "Search historical ownership states and records before/after the focal event.",
        "format": "Search courts, PDFs, spreadsheets, archives, images, registries, and structured feeds.",
        "source_class": "Seek official, local, specialist, adversarial, whistleblower, and field sources.",
        "role": "Separate legal owner, operational controller, beneficiary, and political relationship.",
        "asset_class": "Check property, companies, securities, vessels, aircraft, trusts, IP, and other stores of value.",
        "negative_space": "List records that should exist if the innocent and misconduct hypotheses are each true.",
    }
    return [prompts[k] for k in audit.missing()]


def due_process_red_team(case: CaseRecord, leading_hypothesis_id: str) -> list[str]:
    h = case.hypotheses[leading_hypothesis_id]
    tasks = [
        "Identify the strongest legitimate explanation for each anomalous relationship.",
        "Search for exculpatory records before escalating any allegation.",
        "Check whether apparently independent sources share a single provenance family.",
        "Attempt to disprove entity matches, especially common names and look-alike companies.",
        "Ask what evidence would be expected if the subject were innocent and seek it directly.",
    ]
    if h.falsifier_claim_ids:
        tasks.append("Prioritize falsifier claims before collecting more supporting evidence.")
    return tasks
