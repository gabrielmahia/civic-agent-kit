# Blind backtest protocol

## Purpose

Test whether JICHO discovers useful leads *before* outcomes are known and whether it avoids accusing benign complexity.

## Dataset design

Stratify across:
- regions and languages,
- democracies/autocracies/hybrid systems,
- procurement, bribery, state capture, offshore wealth, sanctions evasion, organized crime, crimes-against-humanity evidence chains,
- successful accountability, failed accountability, partial/captured accountability,
- different decades and data environments.

Required control groups:
1. confirmed misconduct,
2. complex but legitimate structures,
3. false public allegations,
4. investigations that produced no substantiated finding.

## Freeze rule

For each case choose cutoff T.
The system receives only material demonstrably available at or before T.
Later reporting, later entity labels and hindsight annotations are hidden.

## Metrics

- lead time vs historical investigation
- true-positive rate
- false-positive rate
- precision of entity resolution
- alias/jurisdiction/language recall
- coverage-confidence calibration
- time-to-best-discriminating-document
- investigator hours saved
- percentage of material claims with reproducible provenance
- rate at which null hypotheses survive
- correction/exoneration propagation
- corruption displacement detection

## No-cheating rule

A backtest fails if a later-known entity, alias, relationship or scandal keyword leaks into retrieval.

## First case families

Include at minimum:
- Watergate
- Operation Greylord
- Iran-Contra/BCCI
- Goldenberg/Pattni
- Abacha asset recovery
- South African state capture
- 1MDB
- Odebrecht/Lava Jato
- CICIG cases
- Marcos asset recovery
- cartel/trade-based laundering typologies
- Panama/Pandora
- ICTY/ICTR evidence preservation

Add matched benign controls before claiming predictive value.

## Kill conditions

Do not proceed to public deployment if:
- false-positive rate is politically/socially unacceptable,
- provenance cannot be reproduced,
- coverage critic adds cost without measurable recall gains,
- entity resolution regularly merges distinct people/companies,
- subject-rights red team cannot materially change conclusions,
- sensitive-source compartmentation fails.
