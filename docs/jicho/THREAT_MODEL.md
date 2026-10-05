# Threat model

## Threat actors

- corrupt officials and politically exposed networks
- organized crime / money-laundering networks
- litigants seeking to suppress reporting
- partisan actors weaponizing the system
- compromised insiders
- hostile intelligence/security services
- data brokers / doxxers
- ordinary attackers seeking sensitive source information

## Primary failure modes

### Capture
An operator suppresses allied cases or prioritizes opponents.

### Poisoning
Fabricated documents/tips create false graphs.

### Re-identification
Source identities leak through metadata or graph structure.

### Defamation by automation
Model output is presented as fact.

### Entity collision
Two people/entities are wrongly merged.

### Entity fragmentation
One actor is split across aliases and jurisdictions.

### Provenance laundering
Copied reporting appears to be independent corroboration.

### Historical erasure
Deletion/rebranding/jurisdiction change destroys institutional memory.

### Autoimmune behavior
High-recall anomaly systems treat complexity as guilt.

## Controls

- append-only audit log
- cryptographic document hashes
- role-separated administration
- public methodology
- reproducible evidence bundles
- strict evidence-state vocabulary
- right of reply for serious publication
- correction/reversal propagation
- source vault physically/logically separated from public graph
- no raw source identity in model prompts unless indispensable and approved
- periodic blind benign-control testing
- random audits of the detection system itself
- independent capture critic

## Publication boundary

JICHO may publish evidence and documented relationships.
It must not publish model-generated guilt conclusions.

High-risk allegations require:
human editorial review + source verification + subject response + legal review appropriate to jurisdiction.
