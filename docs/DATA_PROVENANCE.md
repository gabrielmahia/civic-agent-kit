# Data provenance and truthfulness

This package has two different data paths. They must not be conflated.

## 1. File-backed loaders

`src/civic_agent_kit/data.py` contains loaders for external CSV files. The county-budget loader points users to the Kenya Civic Datasets Kaggle DOI `10.34740/kaggle/dsv/15473045` when its file is absent. Parliament and SACCO loaders expect local `civic_data/*_seed.csv` files; those files are not present in this repository.

The README links the broader Kenya Civic Datasets on Kaggle and Hugging Face. Those links do **not** establish provenance for the embedded tables described below.

## 2. Embedded MCP demo tables

`src/civic_agent_kit/server.py` contains hard-coded tables named:

- `DROUGHT_DATA`
- `BUDGET_DATA`
- `PARLIAMENT_BILLS`
- `SACCO_DATA`

Their original row-level sources and as-of dates are **not recorded** in this repository. Treat every value in those four tables as **synthetic/sample demo data**, not as an official, historical, or current figure.

The MCP tool responses are intended to label these values as demo/synthetic and point to the relevant real-world institution for users who need authoritative data. Those institution references are discovery pointers, not provenance for the embedded values.

## Constitutional-rights text

`RIGHTS_DB` contains short English/Kiswahili statements keyed to Constitution of Kenya article numbers. This repository does not currently carry a source snapshot, retrieval date, translation provenance, or cryptographic digest for those strings. They should therefore not be treated as a provenance-preserved legal corpus. For consequential legal use, verify against an authoritative current constitutional text.

## Provenance rule for future embedded data

Do not add a factual embedded row unless its provenance can be recorded with, at minimum:

- source organization and source URL or stable identifier;
- source publication/retrieval date or explicit `unknown`;
- license/terms status when known;
- transformation method;
- whether the row is factual, derived, synthetic, or illustrative.

If those fields cannot be established, label the row synthetic/illustrative rather than implying an official source.

This document records what the repository can substantiate; it does not retroactively manufacture provenance that was never captured.
