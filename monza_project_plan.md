# Monza Tyre Strategy Model — Project Plan
**Callum Skinner | 19 Aug – 6 Sept 2026**

---

## The hard constraint

| Milestone | Date |
|---|---|
| Build window opens | Wed 19 Aug (tonight) |
| **Build must be finished** | **Mon 31 Aug** |
| Slack day — float, not extra scope | Tue 1 Sept |
| Packing / dry run | Wed 2 Sept |
| Flight to UK | Thu 3 Sept |
| Monza FP2 — data drops | Fri 4 Sept |
| Qualifying | Sat 5 Sept |
| Race — compare prediction vs reality | Sun 6 Sept |

**Realistic budget: ~27–30 usable hours.** Friday 21st at 3–4 h, then ten days at 2–3 h, minus attrition.

The model must be *finished and validated* before the race weekend. On Friday 4 September you are pressing go, not building. Validation comes from backtesting races already run this season — **not** from Monza.

---

## Operating rules

1. **One deliverable per session.** Never sit down to "work on the project." Sit down to produce the one named output for that block. If you can't state the output in a sentence, you're not ready to start.
2. **Time-box, don't perfect.** A working ugly version on schedule beats an elegant one that isn't finished.
3. **Commit every session.** Even broken code. Git history is evidence of process for your CV.
4. **Split the coding.** You write the modelling logic (with me explaining first). I write the plumbing. Don't burn learning-time on boilerplate.

---

## Schedule

### Tonight — Wed 19 Aug (~30 min)
**Deliverable:** FastF1 installed, one 2026 session pulled, lap dataframe printed to screen.

Nothing else. Just prove the pipe works so a dependency error can't cost you a real block later.

---

### Thu 20 Aug — OFF
Work until 5pm. Write off entirely.

### Block A — Fri 21 Aug (3–4 h, hard stop 16:00 for the airport run)
**Deliverable:** Script that pulls *all* 2026 race weekends and caches them locally.

- Enable FastF1's cache (non-negotiable — re-downloading kills you later)
- Loop the season, pull FP2 + Race sessions
- Save to disk as parquet/CSV
- *I write most of this.*

Set the hard stop at 16:00 and honour it. Do not be babysitting a download when you should be leaving for the airport.

---

### Block B — Sat 22 – Sun 23 Aug (4–6 h)
**Deliverable:** One clean dataframe. Every usable lap, all 2026 races, with compound, tyre age, stint number, driver, team, session.

Filters to apply:
- Drop in-laps and out-laps
- Drop laps under yellow/SC/VSC (`track_status`)
- Drop laps where car ahead is within ~1.5 s
- Drop laps outside a rolling median band per stint

You should expect to discard 30–40% of laps. That is correct, not a bug.

**Checkpoint:** if you finish Block B by end of 23 Aug you are on schedule.

---

### Block C — Mon 24 – Tue 25 Aug (4–6 h)
**Deliverable:** Degradation slope per compound, plotted, with a stated uncertainty band.

1. Fuel correction — estimate burn rate, apply lap-time-per-kg. **Do not skip this.**
2. Linear fit of fuel-corrected lap time vs tyre age, per compound, pooled across the field.
3. Plot it. Look at it. Does the softer compound degrade faster? If not, something upstream is wrong.
4. Run the fit again with fuel-effect assumptions ±30% and record how much the answer moves.

*You write this. It's the core of the project.*

**CHECKPOINT — end of 25 Aug:** if the deg curves aren't producing sensible slopes, cut the backtest from all races to four, and keep going. Do not spend a third day here.

---

### Block D — Wed 26 – Thu 27 Aug (4–6 h)
**Deliverable:** A function that returns ranked strategies by predicted total race time.

- Derive pit loss from data (pit-in + pit-out lap vs that driver's baseline, averaged across the field)
- Enumerate strategies: 1-stop and 2-stop, all valid compound orders, all stop laps
- Total race time = sum of modelled lap times + (stops x pit loss) + (stops x **traffic penalty**)
- Leave the traffic penalty as a free parameter for now

*You write this.*

> **Watch for:** Monza's pit loss is among the lowest on the calendar. Without the traffic penalty, your optimiser will over-recommend stops. That's what the next block calibrates.

---

### Block E — Fri 28 – Sat 29 Aug (4–6 h)
**Deliverable:** Backtest table — your predicted strategy vs what teams actually ran, for every 2026 race so far. Plus a calibrated traffic penalty.

- Run the model on FP2 data only for each past race
- Compare predicted stop count and pit window vs actual
- Tune the traffic penalty until the model reproduces reality
- **Report the misses honestly.** A model with a stated 70% hit rate is credible. One claiming 100% is not.

This block is the credibility of the entire project.

**CHECKPOINT — end of 29 Aug:** if the backtest won't converge, ship with the limitation documented and move on. Do not chase it into September.

---

### Block F — Sun 30 – Mon 31 Aug (4–6 h)
**Deliverable:** The CV artifact. README, clean repo, four or five good plots, a written methodology section.

Must state plainly:
- What the model does
- What data it uses and what it lacks (no tyre temps, no pressures, no wear, no fuel data)
- That the deg model is phenomenological, not physical
- Backtest results including failures
- The Monza prediction, made *before* the race

**BUILD STOPS HERE. 31 August.**

---

### Tue 1 Sept — Slack
Deliberately empty. This day exists to absorb one block running over, or a checkpoint you had to take twice.

If you arrive here on schedule with nothing to catch up on: **take the day off.** Do not use it to add features. The scope-creep temptation on a free day is exactly how projects miss deadlines they were previously going to hit.

---

### Wed 2 Sept — Dry run / packing
No new features. Run the whole pipeline end-to-end on the most recent race's data so that on Friday it is literally one command. Then pack.

---

### Thu 3 Sept — Flight
Nothing.

---

## Race weekend protocol

| Day | Action |
|---|---|
| **Fri 4 Sept** | FP2 ends ~16:00 UK. Pull data, run pipeline, generate prediction. **Timestamp and commit it before qualifying.** |
| **Sat 5 Sept** | Nothing. Do not tweak the model after seeing quali. |
| **Sun 6 Sept** | Watch the race. Log actual strategies. |
| **Mon 7 Sept** | Write the results section — prediction vs reality, what you got right, what you got wrong, why. |

The commit timestamp on Friday is what proves the prediction was genuine. That's the difference between a project and a story.

---

## Scope cuts, in order

If you fall behind, cut in this order:

1. Per-team pace intercept (drop first — pure nice-to-have)
2. Backtest across all races → four representative races
3. Confidence bands → point estimate with a written caveat
4. Non-linear deg fit → keep it linear

**Never cut:** fuel correction, the backtest, or the writeup. Those three are the project.

---

## What "done" looks like

A GitHub repo containing:

- A reproducible pipeline from raw FastF1 data to a strategy recommendation
- A documented degradation model with stated assumptions and error bars
- A backtest with an honest hit rate
- A Monza prediction committed before the race, and a post-race comparison
- A README that a race engineer could read in three minutes and understand what you did and what you didn't

That is a genuinely strong second-year portfolio piece. It is *not* impressive because the model is sophisticated — it isn't. It's impressive because it's validated, honest about its limits, and finished on a deadline.
