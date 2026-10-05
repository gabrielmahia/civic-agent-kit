# Design psychology — Record of Power

## Design objective

The site must maximize four things in sequence:

```
ATTENTION → COMPREHENSION → TRUST → ACTION
```

It must **not** maximize outrage, dwell time, addictive scrolling, or accusation velocity.

## Audience modes

### 1. Scanner
Time budget: 10–30 seconds.
Needs:
- what changed,
- why it matters,
- evidence status,
- direct source path.

### 2. Curious citizen
Time budget: 2–10 minutes.
Needs:
- plain-language case explanation,
- key timeline,
- money/ownership path,
- unresolved questions.

### 3. Journalist / investigator
Time budget: hours.
Needs:
- source documents,
- entity aliases,
- relationship graph,
- export,
- provenance,
- historical states,
- “what evidence next?”

### 4. Auditor / regulator / compliance researcher
Needs:
- structured records,
- legal/evidentiary status,
- jurisdictional links,
- machine-readable identifiers,
- API/export.

### 5. Subject / counsel / critic
Needs:
- exact claim being made,
- source basis,
- right-of-reply record,
- correction/reversal process,
- exculpatory evidence surfaced as prominently as incriminating evidence.

## Two-speed interface

### Brief
The default front door.

Low visual complexity.
Large search.
A small number of high-information updates.
Clear “Why this matters.”
No infinite scroll.
No red guilt scores.
No sensational photography unless evidentially relevant.

### Wire
A dense, text-first, fast-scanning stream inspired by the useful properties of old-school link aggregators:
- high information density,
- obvious chronology,
- minimal interaction cost,
- stable layout,
- direct links,
- source and evidence-state labels,
- keyboard-friendly scanning.

The Wire should feel like a newsroom terminal, **not** a social feed.

### Explore
Search-first investigative interface:
person, entity, contract, asset, jurisdiction, case, evidence.

### Dossier
Progressive disclosure:
1. one-paragraph summary,
2. key evidence,
3. competing explanations,
4. timelines,
5. graph,
6. raw sources / export.

## Research principles

### Credibility is designed before it is argued
Stanford Web Credibility research recommends:
- make accuracy easy to verify,
- show a real organization,
- show expertise,
- make contact easy,
- use professional, purpose-appropriate design,
- make the site useful/easy,
- show recency,
- avoid promotional clutter,
- eliminate errors.

Source:
https://credibility.stanford.edu/guidelines/index.html

### Visual complexity affects first impression almost immediately
Research on website aesthetics found visual complexity and prototypicality affect aesthetic judgments within tens of milliseconds; lower complexity and recognizable structure performed better on first impression.

Reference:
Tuch et al., International Journal of Human-Computer Studies 70(11), 2012.
DOI: 10.1016/j.ijhcs.2012.06.003

### Information scent beats clever taxonomy
Users follow labels that clearly signal where useful information lies.
Top navigation should be topic/task based rather than format based.

Sources:
https://www.nngroup.com/articles/information-scent/
https://www.nngroup.com/articles/format-based-navigation/

Therefore top navigation should say:
- Money
- Contracts
- People
- Companies
- Assets
- Cases
- Wire
- Explore

Not:
- Reports
- Videos
- PDFs
- Databases

### Progressive disclosure reduces cognitive overload
Show the most important facts first; make deeper complexity available without forcing it on everyone.

Source:
https://www.nngroup.com/videos/progressive-disclosure/

## Learning from War & Sanctions

Ukraine's War & Sanctions portal demonstrates the value of:
- broad category coverage,
- search,
- named entity records,
- logistics + finance + companies + individuals in one system,
- sanctions cross-reference,
- update chronology,
- API availability.

Current portal:
https://war-sanctions.gur.gov.ua/en/

Its weakness for our purpose is homepage cognitive density: many category blocks compete for first attention.

Transfer:
- preserve its breadth,
- move breadth behind strong search and Explore,
- expose only the highest-information changes on Home,
- put full taxonomy in Wire/Explore.

## Learning from ICIJ Offshore Leaks

ICIJ deliberately simplified a very complex data system into a single search field and permanent entity pages. It also warns that inclusion in offshore data is not evidence of wrongdoing.

Sources:
https://www.icij.org/inside-icij/2013/06/how-we-built-offshore-leaks-database/
https://offshoreleaks.icij.org/pages/howtouse

Transfer:
- one dominant search field,
- permanent URLs,
- graph exploration on demand,
- explicit non-guilt disclaimer,
- alias-aware search,
- source dataset and date visible.

## Shareability without sensationalism

Create source-linked **evidence cards**:
- factual claim,
- evidence state,
- date,
- source,
- “what remains unknown,”
- permanent URL.

Cards must never detach a claim from its status or provenance.

## Anti-dark-pattern rules

Do not use:
- infinite-scroll outrage loops,
- personalized accusation feeds,
- “people you should hate” recommendations,
- engagement streaks,
- red flashing guilt indicators,
- unlabeled AI-generated summaries,
- hidden corrections,
- manipulative countdowns.

## Metrics

Optimize for:
- search success,
- source-open rate,
- correction visibility,
- comprehension accuracy,
- repeat expert use,
- evidence-to-source click depth,
- time to answer a concrete question,
- successful cross-jurisdiction handoff.

Do not optimize for raw dwell time.
