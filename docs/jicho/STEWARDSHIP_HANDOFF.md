# Stewardship handoff package

## Principle

Do not merely “give someone a website.”

Transfer a reproducible institution-in-a-box:
- code,
- data model,
- operational runbooks,
- governance rules,
- threat model,
- deployment ownership,
- editorial boundaries,
- correction history,
- tests,
- maintenance procedures.

## Candidate steward profiles

### Investigative newsroom
Good fit when the priority is:
- investigations,
- source handling,
- publication,
- cross-border journalism,
- right of reply.

### Anti-corruption civil-society organization
Good fit when the priority is:
- public-finance monitoring,
- advocacy,
- strategic litigation,
- citizen complaints,
- integrity reform.

### Civic-tech/data organization
Good fit when the priority is:
- platform operations,
- datasets,
- APIs,
- forensic/data tooling,
- partner newsroom support.

### Consortium
Likely strongest long-run model:
- editorial partner,
- technology/data partner,
- integrity/legal partner,
with explicit separation of powers.

## Kenyan organizations to evaluate

The following are **candidate conversations, not endorsements or commitments**:

- Africa Uncensored — independent Nairobi investigative media house; OCCRP network member.
- Code for Africa — Kenya-registered public-benefit organization with civic-tech, data-journalism, forensic/OSINT and ANCIR infrastructure.
- Transparency International Kenya — anti-corruption organization with public-finance, advocacy, research, litigation/civic-engagement capacity.
- Mzalendo Trust — non-partisan Kenyan civic-tech/parliamentary accountability organization.
- Ushahidi — Kenyan-rooted open-source civic technology/nonprofit with human-rights and good-governance deployment experience.

The right steward should be chosen by capability and governance fit, not prestige.

## Steward evaluation rubric

Require written answers to:

### Independence
- Who funds the organization?
- Can donors veto investigations?
- What conflict-of-interest rules exist?
- Can government or political actors remove staff or block cases?

### Editorial/due process
- Is there an editor with final responsibility?
- Is right of reply mandatory?
- Is legal review available?
- How are corrections/retractions propagated?

### Source security
- Has the organization handled high-risk sources?
- Are source identities separated from publication data?
- Who can access raw source material?
- What incident-response process exists?

### Technical capacity
- Can it operate GitHub, hosting, DNS, PostgreSQL, backups, CI/CD?
- Can it maintain APIs/data pipelines?
- Does it have on-call capability for security incidents?

### Cross-border reach
- Can it work with OCCRP/ICIJ/ANCIR/foreign reporters?
- Can it route evidence to expertise in other jurisdictions?

### Longevity
- Can it fund maintenance for 5–10 years?
- What happens if a grant ends?
- Can the system survive staff turnover?

## Transfer bundle

Before transfer, provide:

1. Source repository and tagged release.
2. SBOM/dependency inventory.
3. Deployment diagram.
4. Infrastructure-as-code where possible.
5. DNS/domain transfer instructions.
6. Database schema + migration history.
7. Backup/restore runbook.
8. Secret-rotation runbook (never transfer founder secrets).
9. Monitoring/alerting runbook.
10. Security threat model.
11. Editorial/evidence-state policy.
12. Corrections/retractions policy.
13. Source-intake boundary policy.
14. Movement-data policy.
15. Data-source licenses/terms.
16. Historical backtest results.
17. Known limitations/failure modes.
18. Admin/operator handbook.
19. Contributor/AI-agent handbook.
20. 30/60/90-day transition checklist.

## Transfer procedure

### Phase 1 — shadow operation
Recipient runs a staging copy using its own accounts.
Original incubator stays read-only/reference.

### Phase 2 — reproducibility test
Recipient must independently:
- deploy,
- restore backup,
- run tests,
- ingest a public fixture,
- publish/correct a synthetic record.

### Phase 3 — ownership transfer
Transfer:
- domain,
- GitHub organization/repository,
- hosting project,
- monitoring,
- service accounts,
without transferring personal passwords.

Rotate all credentials after transfer.

### Phase 4 — editorial independence
Founding incubator loses unilateral publish/admin rights.
Any future contribution follows the same public contribution process as others.

### Phase 5 — exit
Publish:
- governance,
- funding,
- maintainers,
- contact,
- methodology,
- independence statement.

The handoff is complete when the recipient can operate for 90 days without relying on the original builder.
