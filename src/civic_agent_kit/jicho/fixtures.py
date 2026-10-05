from __future__ import annotations

from .core import CaseRecord, Claim, CoverageAudit, EvidenceState, Hypothesis, Source


def _source(sid: str, family: str, reliability: float = 0.8) -> Source:
    return Source(sid, "mock_fixture", f"fixture://{sid}", family, reliability)


def ghost_road() -> CaseRecord:
    sources = {"award": _source("award","procurement"), "payment": _source("payment","treasury"), "field": _source("field","field_verification"), "company": _source("company","registry")}
    claims = {
        "paid": Claim("paid","County","paid","RoadCo",EvidenceState.DOCUMENTED_DISCREPANCY,("payment",),confidence=.95,coverage_confidence=.8),
        "award": Claim("award","County","awarded_contract_to","RoadCo",EvidenceState.DOCUMENTED_DISCREPANCY,("award",),confidence=.95,coverage_confidence=.8),
        "missing": Claim("missing","RoadProject","physical_outcome","not_observed",EvidenceState.INVESTIGATIVE_FINDING,("field",),confidence=.9,coverage_confidence=.8),
        "newco": Claim("newco","RoadCo","incorporated_shortly_before","award",EvidenceState.DOCUMENTED_DISCREPANCY,("company",),confidence=.85,coverage_confidence=.75),
    }
    hypotheses = {"leading": Hypothesis("leading","public funds may not have produced contracted outcome",("paid","award","missing","newco")), "null": Hypothesis("null","delivery exists but field observation is incomplete",(),("missing",))}
    return CaseRecord("ghost-road","Ghost road contract",sources,claims,hypotheses,CoverageAudit({k:True for k in ("identity","relationships","geography","time","format","source_class","role","negative_space")}),"investigate")


def legitimate_joint_venture() -> CaseRecord:
    sources = {"award": _source("award","procurement"), "registry": _source("registry","registry"), "delivery": _source("delivery","independent_engineer"), "finance": _source("finance","audited_financials")}
    claims = {
        "complex": Claim("complex","JV","has_offshore_parent","yes",EvidenceState.DOCUMENTED_DISCREPANCY,("registry",),confidence=.95,coverage_confidence=.85),
        "delivery": Claim("delivery","Project","delivered","yes",EvidenceState.OFFICIAL_FINDING,("delivery",),confidence=.95,coverage_confidence=.9),
        "finance": Claim("finance","JV","financing_reconciles","yes",EvidenceState.OFFICIAL_FINDING,("finance",),confidence=.9,coverage_confidence=.85),
        "award": Claim("award","Agency","competitive_award","yes",EvidenceState.OFFICIAL_FINDING,("award",),confidence=.9,coverage_confidence=.85),
    }
    hypotheses = {"leading": Hypothesis("leading","offshore complexity conceals misconduct",("complex",),("delivery","finance","award")), "null": Hypothesis("null","complex but legitimate transaction",("delivery","finance","award"))}
    return CaseRecord("legit-jv","Complex legitimate joint venture",sources,claims,hypotheses,CoverageAudit({k:True for k in ("identity","relationships","geography","language","time","format","source_class","role","asset_class","negative_space")}),"do_not_escalate")


def alias_shell() -> CaseRecord:
    sources = {"contract": _source("contract","procurement"), "registry1": _source("registry1","registry_alpha"), "registry2": _source("registry2","registry_beta"), "bankruptcy": _source("bankruptcy","court")}
    claims = {
        "award": Claim("award","Agency","awarded_contract_to","Aabar Example PJS Limited",EvidenceState.DOCUMENTED_DISCREPANCY,("contract",),confidence=.95,coverage_confidence=.75),
        "lookalike": Claim("lookalike","Aabar Example PJS Limited","name_nearly_matches","Aabar Example PJS",EvidenceState.DOCUMENTED_DISCREPANCY,("registry1","registry2"),confidence=.95,coverage_confidence=.8),
        "unrelated": Claim("unrelated","Aabar Example PJS Limited","not_affiliated_with","Aabar Example PJS",EvidenceState.INVESTIGATIVE_FINDING,("registry1","registry2"),confidence=.9,coverage_confidence=.8),
        "benefit": Claim("benefit","Funds","later_appear_in","related_asset_proceeding",EvidenceState.CORROBORATED_ALLEGATION,("bankruptcy",),confidence=.72,coverage_confidence=.65),
    }
    hypotheses = {"leading": Hypothesis("leading","look-alike entity warrants tracing",("award","lookalike","unrelated","benefit")), "null": Hypothesis("null","similar name is coincidence",(),("unrelated",))}
    return CaseRecord("alias-shell","Look-alike entity",sources,claims,hypotheses,CoverageAudit({k:True for k in ("identity","relationships","geography","time","format","source_class","role","negative_space")}),"investigate")


def false_allegation() -> CaseRecord:
    sources = {"viral": _source("viral","social_media",.25), "registry": _source("registry","registry",.9), "audit": _source("audit","auditor",.9)}
    claims = {
        "viral": Claim("viral","Official","secretly_owns","Supplier",EvidenceState.LEAD,("viral",),confidence=.25,coverage_confidence=.25),
        "registry": Claim("registry","Official","ownership_link","none_found",EvidenceState.OFFICIAL_FINDING,("registry",),confidence=.85,coverage_confidence=.8),
        "audit": Claim("audit","Contract","delivery_and_price_verified","yes",EvidenceState.OFFICIAL_FINDING,("audit",),confidence=.9,coverage_confidence=.85),
    }
    hypotheses = {"leading": Hypothesis("leading","official secretly owns supplier",("viral",),("registry","audit")), "null": Hypothesis("null","viral allegation is unsupported",("registry","audit"))}
    return CaseRecord("false-allegation","False allegation control",sources,claims,hypotheses,CoverageAudit({k:True for k in ("identity","relationships","geography","language","time","format","source_class","role","negative_space")}),"do_not_escalate")


def all_cases() -> list[CaseRecord]:
    return [ghost_road(), legitimate_joint_venture(), alias_shell(), false_allegation()]
