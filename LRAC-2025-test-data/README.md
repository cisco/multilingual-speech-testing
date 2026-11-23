# LRAC Challenge 2025 (LRAC 1.0) Test Data

Test data for the [Low-Resource Audio Codec (LRAC) Challenge 2025 (LRAC 1.0)](https://crowdsourcing.cisco.com/lrac-challenge/2025/).

- [`open-test-set/`](open-test-set/): clean, noisy and reverberant speech with clean references, for objective evaluation.
- [`blind-test-set/`](blind-test-set/): predominantly real-world recordings, for human listening tests. See its [README](blind-test-set/README.md) for folder structure and data sources.

Each set is split by challenge track (`track_1`, `track_2`).

For blind test set licensing and attribution, see [`blind-test-set/README.md`](blind-test-set/README.md); the `meta.csv` files in each subset folder provide per-file license identifiers. For open test set licensing, see the `meta.csv` files in each subset folder (`speech_src_license`, `noise_src_license`, `rir_src_license` columns).
