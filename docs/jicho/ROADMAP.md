# Roadmap

## Phase 0 — Incubation (now)
- freeze doctrine
- freeze claim/evidence model
- freeze threat model
- define first blind backtest corpus
- choose public brand/domain
- keep sensitive-source handling out of MVP

## Phase 1 — Backtest harness
Build ingestion + claim store + entity resolver + coverage critic.
Run historical cases and matched benign controls.
No public accusation features.

Success gate:
measurable recall improvement from Coverage Critic without unacceptable false positives.

## Phase 2 — Kenya public-money MVP
Public/open data only:
- procurement/OCDS
- Auditor-General reports
- company/public ownership records where lawful
- Kenya Law/court records
- public sanctions/debarment records
- project physical-verification fields

Outputs:
contract pages, entity pages, evidence pages, missing-record detector.

## Phase 3 — Reporter workspace
Private case workspaces:
- hypothesis ledger
- rival/null models
- ATI/FOIA drafting
- document triage
- cross-jurisdiction routing
- right-of-reply packet generation

Source vault remains separate.

## Phase 4 — Cross-border federation
Exchange selected claims/entities/evidence bundles with partner newsrooms/NGOs without centralizing source identities.

## Phase 5 — Public accountability memory
Publish append-only historical case records and corrections.
Support portable case/entity IDs.

## Immediate engineering backlog

1. Implement claim/event tables.
2. Implement source/document hashing.
3. Map OCDS parties/contracts into claim model.
4. Add entity alias table with MERGE/SPLIT review workflow.
5. Build coverage-audit checklist service.
6. Build historical time-freeze fixture loader.
7. Create five corrupt + five benign backtest fixtures.
8. Prototype contract-to-outcome page.
9. Prototype three-clock case timeline.
10. Add correction/reversal event propagation.
