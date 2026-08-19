# F1 Tyre Strategy Model — 2026 Italian Grand Prix

A tyre degradation and pit strategy model built from publicly available Formula 1 timing data,
used to produce a pre-race strategy prediction for the 2026 Italian Grand Prix (Monza, 4–6 September)
and validated by backtesting against races already run in the 2026 season.

**Author:** Callum Skinner — BEng Motorsport Engineering, Oxford Brookes University

---

## Status

> Work in progress. Prediction to be committed before qualifying on 5 September 2026.

---

## What this does

1. Pulls timing data for the 2026 season via [FastF1](https://docs.fastf1.dev/)
2. Filters to representative green-flag laps and fuel-corrects them
3. Fits a degradation model per tyre compound, pooled across the field
4. Derives pit loss empirically from measured pit in/out laps
5. Enumerates candidate strategies and ranks them by predicted total race time
6. Backtests against completed 2026 races to calibrate a traffic penalty term
7. Produces a strategy prediction for Monza

## What this does not do

This is a **phenomenological model, not a physical one.** It fits observed lap time loss against
tyre age. It has no access to:

- Tyre pressures, carcass or surface temperatures
- Actual tyre wear (tread depth)
- Fuel loads (estimated, not measured)
- Car setup or aerodynamic configuration

It therefore cannot separate thermal degradation from wear degradation, and cannot predict
graining or blistering onset. Results should be read with that limitation in mind.

## 2026 regulation change

2026 introduced new car and tyre regulations. Pre-2026 data is **not** used, because tyre
dimensions, car mass and aerodynamic load distribution all changed simultaneously and their
effects cannot be separated retrospectively.

---

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
pip install -r requirements.txt
```

## Repository structure

```
f1-project/
├── data/
│   ├── raw/            # FastF1 cache (gitignored)
│   └── processed/      # cleaned dataframes (gitignored)
├── src/
│   ├── load_data.py    # session pulls + caching
│   ├── clean.py        # lap filtering
│   ├── degradation.py  # fuel correction + deg model
│   ├── strategy.py     # pit loss + strategy optimiser
│   └── backtest.py     # validation against completed races
├── notebooks/          # exploration
├── outputs/            # figures and results
└── monza_project_plan.md
```

---

## Results

_TBC — backtest hit rate and Monza prediction vs actual to be added._

## Method

_TBC — see project plan._
