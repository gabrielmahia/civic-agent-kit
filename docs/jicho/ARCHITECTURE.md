# Architecture

## Seven engines

### 1. Reality Engine
Reconciles:
```
budget → authorization → procurement → supplier → payment → delivery → physical outcome
```
The terminal question is often physical: did the road, medicine, school, service or equipment actually exist?

### 2. Graph Engine
Represents people, entities, contracts, assets, addresses, roles, jurisdictions and relationships. Preserve competing assertions instead of silently choosing one.

Align where practical with:
- Open Contracting Data Standard (OCDS)
- OCCRP FollowTheMoney concepts
- OpenSanctions entity patterns
- W3C PROV-like provenance concepts

### 3. Coverage Critic
Independent from the investigator. It attacks omissions across:
identity, geography, language, time, format, source class, role, asset type, relationships and negative space.

### 4. Due-Process Red Team
Works against the leading allegation. Searches for:
legitimate sources of wealth, mistaken identity, benign procurement explanations, contradictory witnesses, incomplete context, procedural defects and exculpatory records.

### 5. Routing Engine
Finds the cheapest lawful next evidence and the right capability:
local reporter, foreign reporter, ATI/FOIA request, registry expert, auditor, procurement analyst, field verification, court-record researcher.

### 6. Accountability Memory
Append-only state transitions:
```
allegation → evidence → counterevidence → finding → adjudication → appeal → correction → outcome
```
Never overwrite history. Append corrections.

### 7. Institutional-Capture Critic
Assumes JICHO itself may be targeted. Audits for:
selective suppression, fabricated tips, entity-match manipulation, source exposure, model-threshold tampering, partisan case selection and deletion.

## Bidirectional reconstruction

Run two investigations toward each other:

**Public funds forward**
```
budget → contract → supplier → intermediary → asset
```

**Private wealth backward**
```
asset → owner → entity → financier → counterparty → source of capital
```

A convergence raises investigative priority; it does not prove wrongdoing.

## Storage principle

Use a federated architecture for sensitive journalism:
- public evidence graph may be shared,
- newsroom/source vaults stay separate,
- source identities never enter the public graph,
- cross-node exchange uses selected claims/documents rather than full vault replication.

## Suggested implementation stack

MVP:
- Python ingestion/analysis services
- PostgreSQL + JSONB for claims/entities/events
- object storage for documents with SHA-256 hashes
- full-text search (Postgres initially; OpenSearch later)
- Next.js/TypeScript public interface
- OIDC authentication for authenticated workspaces
- background jobs for ingestion/entity-resolution
- graph projection layer derived from the authoritative claim store

Do not make a graph database the system of record. The authoritative unit is a provenance-bearing assertion/event.
