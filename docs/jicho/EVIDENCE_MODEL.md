# Evidence model

## Fundamental unit: assertion

Do not store “Person A owns Company B” as an unqualified fact.

Store:
- subject
- predicate
- object/value
- valid time
- asserted time
- source
- source locator
- direct vs inferred
- confidence
- corroboration
- contradictions
- reviewer
- status
- supersedes / corrected-by links

## Public evidence states

1. **Lead** — unverified; restricted workspace only.
2. **Corroborated allegation** — multiple independent signals, unresolved.
3. **Documented discrepancy** — primary records establish an inconsistency.
4. **Investigative finding** — reporting supports a conclusion after adversarial review/right of reply.
5. **Official finding** — regulator, commission, court or auditor formally rules.
6. **Sanction/debarment** — competent authority imposes administrative consequence.
7. **Conviction** — criminal liability adjudicated.
8. **Cleared/reversed/corrected** — later evidence or process changes status.

Statuses are not a one-way ladder. They can reverse.

## Provenance requirements

For every material public claim retain:
- source URL / archive identifier / document ID
- publisher/issuer
- original date
- retrieval date
- exact page/line/cell locator where available
- file hash where a document is retained
- transformation notes (OCR, translation, extraction)
- independence assessment for corroborating sources

## Independence rule

Ten stories copying the same allegation are one source family, not ten confirmations.

## Identity model

Maintain separately:
- legal identity
- operational controller
- economic beneficiary
- public/political relationship

Never infer one from another automatically.

## Corrections

Publication should be irreversible in history but reversible in interpretation:
- do not delete the old state,
- append correction/reversal,
- recompute current display state,
- preserve who changed what and why.

See schema/claim.schema.json.
