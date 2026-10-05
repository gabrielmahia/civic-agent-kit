# Mock test results — JICHO v0

Date: 2026-10-04

A first executable smoke test was run locally against four synthetic fixtures. This is **not** a validation of real-world predictive power; it only tests whether the architecture can represent leading/null hypotheses, coverage gaps, due-process checks and escalation boundaries without collapsing complexity into guilt.

## Fixtures

| Fixture | Expected | Prototype result | Coverage |
|---|---:|---:|---:|
| Ghost road contract | investigate | investigate | 0.80 |
| Complex legitimate joint venture | do not escalate | do not escalate | 1.00 |
| Look-alike entity | investigate | investigate | 0.80 |
| False allegation control | do not escalate | do not escalate | 0.90 |

Unit tests: **4 passed / 4 total**.

## What this proves

- the model can carry answer confidence separately from coverage confidence;
- benign controls can defeat an attractive misconduct hypothesis;
- low-state viral allegations are blocked by the publication guard;
- the Coverage Critic can emit unsearched evidence classes;
- a look-alike-entity fixture can be escalated without treating similarity as guilt.

## What this does *not* prove

- no real-world precision/recall claim;
- no historical lead-time claim;
- no cross-language entity-resolution claim;
- no protection against dataset poisoning/capture yet;
- no legal/publication readiness.

## Next discriminating test

Construct frozen-time historical fixtures plus matched legitimate controls. The first serious benchmark should contain at least 20 positive and 20 negative/benign cases before any public-risk score or automated allegation surface is considered.
