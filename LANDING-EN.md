# Backtest in 100 Lines — free download

**Title:** Backtest in 100 Lines (free)
**Subtitle:** Your first honest backtest in under a minute. A self-contained Python script + real BTC data + 10 LLM prompts to generate your first trading ideas.

---

### Why this is free

Because the first lesson of quantitative trading is worth more than the
first dollar: **a backtest is only as honest as its timing and cost
rules.** This starter bakes in the two rules most "strategy screenshots"
ignore — no look-ahead (signals from day t apply from day t+1) and
transaction costs on every position change — so the numbers you see are
numbers you can actually trust.

### What's inside

- `mini_backtest.py` — a commented, self-contained SMA 50/200 backtest
  you can edit in any editor
- `sample_btc.csv` — 4.8 years of real BTC/USD daily data (2022–2026)
- `mini_report.md` + `equity_curve.png` — generated after one command
- `prompts/starter_prompts.md` — 10 LLM prompts to generate and
  pressure-test your first hypotheses

### One command

```bash
python mini_backtest.py
```

That's it. Python 3.10+ with numpy and pandas. No API keys, no accounts.

### The honest numbers (sample run, 2022–2026, 10 bps costs)

| | Strategy (SMA 50/200) | Buy & hold |
| --- | --- | --- |
| Total return | +91.1% | +69.2% |
| Max drawdown | -39.6% | -66.7% |
| Sharpe | 0.57 | 0.47 |

The crossover halved the drawdown here — but only after costs, only in
this sample, and it still lost 40% at its worst. That tension is the
whole game.

### The upgrade path

If this script makes you want the real machinery — 5 strategy families,
walk-forward validation, risk overlays, trade autopsy, 30 full research
prompts, and the Anti-Overfitting Playbook — that's the **Quant Research
Template Pack**, available wherever you found this download.

---

*Not financial advice. Past performance does not predict future results.*
