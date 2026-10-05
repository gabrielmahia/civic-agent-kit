# Independence and governance

## Principle

**Independence must be structural, not cosmetic.**

A site cannot honestly claim to be fully independent merely because the founder's name is absent from the footer.

## Public separation from the incubator

The public-facing product should eventually have:
- its own legal/organizational identity,
- its own domain,
- its own project email addresses,
- its own GitHub organization,
- its own hosting account,
- its own analytics account,
- its own funding disclosures,
- its own editorial charter,
- its own corrections policy,
- its own governance/oversight.

The current `gabrielmahia/civic-agent-kit` branch is **incubation only**.

## Domain ownership

WHOIS privacy reduces public exposure but does not make a registrant anonymous to the registrar.

Cloudflare Registrar redacts most personal WHOIS fields where registry rules permit, but Cloudflare retains the authoritative registrant record and public records may still expose state/province and country.

Reference:
https://developers.cloudflare.com/registrar/account-options/whois-redaction/

Squarespace also provides WHOIS privacy for most supported domains.

Reference:
https://support.squarespace.com/hc/en-us/articles/205812438-Whois-privacy

Therefore Cloudflare is recommended mainly for:
- strong DNS/security integration,
- DNSSEC,
- at-cost registration,
- WHOIS redaction,
not because it makes ownership untraceable.

## End-state ownership

If Record of Power is meant to be institutionally independent, transfer domain/repository/hosting ownership to the independent organization once it exists.

Do not:
- falsify registrar information,
- use nominee identities merely to hide beneficial control,
- misrepresent who legally owns the project.

## Messenger credibility

A founder-personality model is deliberately avoided.

Public trust should come from:
- transparent methodology,
- reproducible sources,
- named editorial standards,
- governance,
- corrections,
- independent contributors/partners,
- funding disclosure,
- auditable provenance.

## Governance safeguards

Recommended before publishing serious allegations:
- editorial lead,
- independent legal review pathway,
- conflicts-of-interest policy,
- source-protection policy,
- corrections/retractions policy,
- outside advisory/oversight group,
- documented recusal mechanism.

## Funding

Every material funder should be disclosed.
No donor should have case-selection or editorial veto rights.

## Technical independence

Production should not depend on one person's:
- personal Google account,
- personal GitHub account,
- personal Cloudflare account,
- personal email,
- personal payment method beyond temporary incubation.

Migration plan:
1. incubate privately,
2. create organization,
3. transfer repository/domain,
4. rotate credentials,
5. publish governance/funding information,
6. then launch public accountability records.
