# Multi-agent collaboration protocol

## Goal

Allow ChatGPT, Claude, Gemini, Grok, Muse, Work/Astra, coding agents, and future models to work on the same project in parallel **without relying on shared chat memory** and without duplicating/destructively overwriting one another.

The core rule is:

> **Git is the memory bus. GitHub Issues/PRs are the coordination bus. Reality/tests are the authority.**

Model agreement is not evidence.

## Cold-start sequence for any agent

1. Read `AGENTS.md`.
2. Read `agent-context.json`.
3. Read the JICHO doctrine/architecture/backtest/threat-model docs.
4. Inspect open Issues.
5. Inspect open and draft PRs.
6. Run baseline tests before changing anything.
7. Claim exactly one bounded workstream.
8. Open a draft PR immediately.

## Why draft PRs are the lock

Shared coordination files create merge conflicts and stale state. A draft PR is:
- visible to every Git-capable agent,
- branch-scoped,
- reviewable,
- mergeable,
- naturally linked to a diff,
- durable after chat context disappears.

Therefore **an open draft PR is the authoritative work claim**.

## Claim format

Branch:
```
agent/<agent-name>/<issue-number>-<slug>
```

Draft PR title:
```
[CLAIM #<issue>] <agent-name>: <scope>
```

PR body:
```markdown
## Objective
...

## Scope owned
- ...

## Explicit non-scope
- ...

## Baseline
- commands run
- results

## Decisions/assumptions
- ...

## Handoff
- current state
- failures/unknowns
- exact next command
```

## Collision protocol

If another PR already touches the same files or solves the same issue:

**Do not duplicate it.**

Choose one:
1. review/red-team/test the existing PR,
2. take a non-overlapping subtask,
3. choose another issue,
4. coordinate through PR comments and explicitly divide files.

No agent should “race” another agent to a merge.

## Workstream decomposition

Prefer parallel tasks with low file overlap:

### A. Historical backtest
Owns:
- frozen-time fixture metadata,
- benchmark metrics,
- positive/negative case sets.

Avoid:
- production UI,
- ingestion runtime.

### B. Public data ingestion
Owns:
- OCDS/PPRA adapters,
- Auditor-General/public-record adapters,
- normalization tests.

### C. Entity resolution
Owns:
- alias/transliteration logic,
- MERGE/SPLIT review,
- identity confidence tests.

### D. Coverage/Due-process critics
Owns:
- blind-spot enumeration,
- falsification prompts,
- benign-explanation search logic.

### E. Website
Owns:
- Brief/Wire/Explore/Dossier UI,
- accessibility,
- low-bandwidth rendering.

### F. Provenance/storage
Owns:
- claims/events,
- document hashes,
- correction propagation,
- audit logs.

### G. Security/governance
Owns:
- source separation,
- capture threat model,
- handoff/governance standards.

## Review roles

A different model should review high-impact work where possible.

Recommended pairings:
- one agent builds,
- second agent attacks assumptions,
- third agent runs/tests against controls.

Do not use model “votes.” Record disagreements as:
```
claim → evidence for → evidence against → falsifier → test
```

## Agent capability declaration

PR authors should say what they can/cannot access:
- repository write access,
- web,
- shell/tests,
- external connectors,
- secrets (normally none),
- historical corpus.

This prevents another agent assuming a task was verified when it was only reasoned about.

## Destructive actions

Require explicit human approval before:
- deleting published data,
- changing licenses,
- publishing allegations about real people,
- enabling source intake,
- changing domain ownership,
- contacting institutions in the founder's voice,
- merging JICHO into stable `main`,
- deploying real-time person-location features.

## Handoff quality bar

A handoff is complete only if a cold agent can:
1. reproduce the current result,
2. identify current failures,
3. find the next task,
4. run the next command,
without reading the previous chat.

## Cross-project standard

This protocol should become a reusable portfolio standard in `nairobi-stack`.
The mechanism remains deliberately provider-neutral: it should work whether the coding agent is OpenAI, Anthropic, Google, xAI, an open-weight local model, or a future system.
