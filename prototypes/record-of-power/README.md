# Record of Power — static prototype

This is a dependency-free public-interface prototype using **synthetic demonstration data only**.

Preview locally:

```bash
cd prototypes/record-of-power
python -m http.server 8000
```

Then open http://localhost:8000.

The prototype demonstrates:
- answer confidence vs coverage confidence,
- legal/evidentiary/narrative clocks,
- evidence-state labels,
- rival/null explanations,
- highest-value next evidence,
- append-only corrections language,
- no guilt scoring.

It is intentionally not connected to a production database or source-intake system.
