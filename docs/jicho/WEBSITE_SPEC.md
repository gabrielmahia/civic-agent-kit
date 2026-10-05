# Website specification

## Product promise

**See the record. Follow the evidence. Preserve the history.**

The public site is an evidence-navigation interface, not a scandal feed.

## Experience model: two-speed interface

### Brief
Default homepage experience:
- one dominant search field,
- small number of high-information changes,
- plain-language “why this matters,”
- explicit evidence state,
- no infinite scroll,
- calm visual hierarchy.

### Wire
Dense, text-first chronological stream for power users:
- stable layout,
- high information density,
- source labels,
- evidence-state labels,
- timestamps,
- direct permanent links,
- keyboard-friendly scanning.

The Wire borrows the useful scanning properties of old-school link aggregators without becoming a sensational headline board.

### Explore
Search and filter by:
person, company, public body, contract, asset, jurisdiction, case, evidence, date.

### Dossier
Progressive disclosure:
1. one-paragraph summary,
2. key evidence,
3. competing explanations,
4. legal/evidentiary/narrative clocks,
5. money/ownership/relationship graphs,
6. travel/assets where relevant,
7. raw documents/export.

See `DESIGN_PSYCHOLOGY.md`.

## Primary surfaces

### Home / Brief
- search entities/cases/contracts
- “what changed” public-interest updates
- evidence state beside every update
- “How evidence works” explainer
- methodology and corrections prominent

### Wire
- chronological updates
- no personalization required
- no engagement ranking
- stable dense text layout
- filters by topic/jurisdiction/evidence state

### Explore
Search by:
person, company, public body, contract, asset, jurisdiction, date.

### Case page
Three synchronized timelines:
1. legal clock
2. evidentiary clock
3. narrative/public-framing clock

Show:
- confirmed facts first
- unresolved allegations distinctly styled
- key documents
- rival explanations
- right-of-reply responses
- current status
- correction history
- “what would change this conclusion?”

### Entity page
- aliases / transliterations / former names
- legal identity
- roles
- linked entities
- jurisdictions
- evidence-backed relationships only
- clear warning that association ≠ misconduct

### Contract / public-money page
```
budget → award → payment → supplier → ownership → delivery → observed outcome
```
Show missing expected records and physical verification status.

### Evidence page
Document viewer with:
source, issuer, date, archive link, hash, extraction/translation notes, claim links.

### Travel / movement
Historical/delayed public-interest movement only.
See `MOVEMENT_DATA_POLICY.md`.

### Methodology
Publish doctrine, evidence states, correction policy, source-independence rule and blind-spot methodology.

### Corrections
First-class searchable corrections/reversals ledger.

### Secure tips
Separate application/security boundary from the public site. Do not build source intake into the same database.

## UX rules

- never use red “guilty” scores
- distinguish allegation / finding / conviction visually and verbally
- show answer confidence separately from coverage confidence
- expose provenance one click from every material claim
- show “what would change this conclusion?”
- accessibility and low-bandwidth mode are requirements
- English + Kiswahili in Kenya MVP; localization architecture from day one
- no hidden primary navigation
- topic/task labels before format labels
- progressive disclosure for complex records
- evidence cards must preserve provenance when shared
- no real-time person tracking
- no infinite-scroll outrage feed

## Visual direction

Calm, documentary, institutional—not sensational.

Target first impression:
- low visual complexity,
- strong typographic hierarchy,
- recognizable news/research conventions,
- near-zero decorative chrome,
- high information scent.

Use maps, timelines and relationship graphs only when they clarify evidence.
Default typography should feel closer to a court record / serious newsroom / wire terminal than a social feed.

## Institutional messenger

The public brand is **Record of Power**, not a founder personality.

Credibility should come from:
- reproducible sources,
- transparent methodology,
- real governance,
- funding disclosure,
- corrections,
- contributor/editor expertise,
- reliable contact paths.

See `INDEPENDENCE_AND_GOVERNANCE.md`.

## Suggested web stack

Next.js + TypeScript
PostgreSQL API
server-rendered public pages
search endpoint
graph visualization loaded on demand
static export for methodology/archive pages
structured metadata for entities/cases/documents
