# Website specification

## Product promise

**See the record. Follow the evidence. Preserve the history.**

The public site is an evidence-navigation interface, not a scandal feed.

## Primary surfaces

### Home
- search entities/cases/contracts
- “How evidence works” explainer
- current public-interest investigations/data projects
- methodology and corrections prominent

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

## Visual direction

Calm, documentary, institutional—not sensational.
Use maps, timelines and relationship graphs only when they clarify evidence.
Default typography should feel closer to a court record / serious newsroom than a social feed.

## Suggested web stack

Next.js + TypeScript
PostgreSQL API
server-rendered public pages
search endpoint
graph visualization loaded on demand
static export for methodology/archive pages
structured metadata for entities/cases/documents
