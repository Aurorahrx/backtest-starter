# backtest-starter

A single-file crypto backtest in ~100 lines of Python: no lookahead bias, real transaction costs, and a buy & hold benchmark — so you can see for yourself what actually survives costs.

**Educational only. Not financial advice.**

## What's inside

- `mini_backtest.py` — self-contained backtest (pandas + numpy only):
  - SMA 50/200 crossover strategy
  - **No lookahead**: signals use only bars up to and including the current close; the position set at bar *t* earns returns from bar *t+1*
  - **Real costs**: configurable cost per side (`COST_BPS`, default 10 bps ≈ taker fee + slippage)
  - **Buy & hold benchmark** printed side by side: return, CAGR, Sharpe, max drawdown, volatility, exposure
- `sample_btc.csv` — real BTC/USD daily data (2022-01-01 → 2026-10-24)
- `prompts/starter_prompts.md` — 10 research prompts to turn this toy into a real workflow
- `JP/` — Japanese intro, disclaimer, and article drafts

## Quick start

```bash
pip install pandas numpy
python mini_backtest.py
```

Free download (pay-what-you-want, $0+): <https://3646932072370.gumroad.com/l/omxtno> — or grab the release zip on this repo's Releases page.

Example output (BTC/USD 2022-01-01 → 2026-10-24, 10 bps/side):

```
  Strategy       return   91.10%  CAGR  14.39%  Sharpe   0.57  maxDD  -39.56%
  Buy & hold     return   69.17%  CAGR  11.54%  Sharpe   0.47  maxDD  -66.74%
```

> One market, one period, one simple strategy. A single positive example proves nothing —
> that's the point. Before you trust any strategy: walk-forward, deflated Sharpe,
> multiple markets, and cost sensitivity. The prompts in `prompts/` walk you through it.

## Disclaimer

This repository is for education and research tooling. Nothing here is investment advice,
a recommendation, or a promise of future returns. Past performance does not predict future
results. Trading crypto involves substantial risk of loss. If you publish work based on this
code, keep it educational and never promise returns.

## License

MIT
