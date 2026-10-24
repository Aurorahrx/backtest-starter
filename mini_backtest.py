"""
Mini Backtest in ~100 Lines — free starter from the Quant Research Template Pack.

What this does:
    1. loads daily OHLCV data (sample BTC/USD included),
    2. builds a classic 50/200 SMA crossover strategy,
    3. backtests it with three honest rules baked in:
         - signals from day t are held from day t+1   (no look-ahead),
         - every position change pays transaction costs,
         - results are compared against buy & hold.

Run:
    python mini_backtest.py

Output:
    mini_report.md   - the full metric table
    equity_curve.png - strategy vs buy-and-hold (if matplotlib is installed)

Why it exists:
    This is the "gateway" version of the full Quant Research Template Pack
    (5 strategy families, walk-forward validation, risk overlays, 30 LLM
    research prompts). If you finish this file and want the honest
    machinery around it, see the README.

Not financial advice. Past results do not predict future returns.
"""

from __future__ import annotations

import os

import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "sample_btc.csv")

# --- configuration (play with these!) -------------------------------------
FAST = 50        # fast moving average, days
SLOW = 200       # slow moving average, days
COST_BPS = 10.0  # transaction cost per position change, basis points
INITIAL = 10_000.0
ANN = 365        # crypto trades every day


def load(path: str) -> pd.DataFrame:
    df = pd.read_csv(path, parse_dates=["date"], index_col="date")
    df.index = pd.DatetimeIndex(df.index)
    return df.sort_index()


def compute_metrics(returns: pd.Series) -> dict:
    equity = INITIAL * (1.0 + returns).cumprod()
    total = equity.iloc[-1] / INITIAL - 1.0
    years = len(returns) / ANN
    cagr = (1.0 + total) ** (1.0 / years) - 1.0
    vol = returns.std(ddof=1) * np.sqrt(ANN)
    sharpe = returns.mean() / returns.std(ddof=1) * np.sqrt(ANN)
    dd = (equity / equity.cummax() - 1.0)
    max_dd = dd.min()
    return {
        "total_return": total, "cagr": cagr, "ann_vol": vol,
        "sharpe": sharpe, "max_dd": max_dd,
        "n_days": len(returns), "n_years": years, "equity": equity,
    }


def backtest(close: pd.Series) -> tuple[pd.Series, pd.Series, dict]:
    """SMA crossover with next-bar execution and costs."""
    ret = close.pct_change().dropna()

    fast_ma = close.rolling(FAST, min_periods=FAST).mean()
    slow_ma = close.rolling(SLOW, min_periods=SLOW).mean()
    # Signal at close of day t: 1 = in the market, 0 = out.
    signal = (fast_ma > slow_ma).astype(float)

    # Held position during day t is yesterday's signal (no look-ahead).
    held = signal.shift(1).fillna(0.0)
    gross = held * ret

    # Pay costs whenever the position changes (including the first entry).
    turnover = signal.diff().abs().fillna(signal.abs())
    costs = turnover * COST_BPS / 1e4

    net = gross - costs
    equity = INITIAL * (1.0 + net).cumprod()

    m = compute_metrics(net)
    m["exposure"] = float((held > 0).mean())
    return net, equity, m


def fmt_row(label: str, m: dict) -> str:
    return (f"  {label:<14} return {m['total_return']:8.2%}  CAGR {m['cagr']:7.2%}  "
            f"Sharpe {m['sharpe']:6.2f}  maxDD {m['max_dd']:8.2%}  "
            f"vol {m['ann_vol']:6.2%}  exposure {m['exposure']:6.0%}")


def main() -> None:
    df = load(DATA)
    close = df["close"]
    ret = close.pct_change().dropna()

    net, equity, m = backtest(close)
    bh_equity = INITIAL * (1.0 + ret).cumprod()
    bh = compute_metrics(ret)
    bh["exposure"] = 1.0

    print(f"\nMini backtest: SMA {FAST}/{SLOW} on {os.path.basename(DATA)} "
          f"({close.index[0].date()} -> {close.index[-1].date()})")
    print(fmt_row("Strategy", m))
    print(fmt_row("Buy & hold", bh))
    print(f"\nFull report: {os.path.join(HERE, 'mini_report.md')}")

    lines = [
        "# Mini Backtest Report — SMA 50/200 on BTC/USD (sample data)",
        "",
        f"_Generated from `mini_backtest.py` (free starter). "
        f"Costs {COST_BPS:.0f} bps per position change. Not financial advice._",
        "",
        "| Metric | Strategy | Buy & hold |",
        "| --- | --- | --- |",
    ]
    keys = [("total_return", "Total return"), ("cagr", "CAGR"),
            ("sharpe", "Sharpe (rf=0)"), ("max_dd", "Max drawdown"),
            ("ann_vol", "Ann. volatility"), ("exposure", "Time in market"),
            ("n_years", "Years")]
    for key, label in keys:
        s, b = m[key], bh[key]
        if isinstance(s, float):
            s, b = f"{s:.2%}", f"{b:.2%}"
        lines.append(f"| {label} | {s} | {b} |")
    with open(os.path.join(HERE, "mini_report.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")

    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.plot(equity.index, equity.values, label="SMA cross", linewidth=1.4)
        ax.plot(bh_equity.index, bh_equity.values, label="Buy & hold", linewidth=1.1, alpha=0.75)
        ax.set_title("Mini backtest: SMA 50/200 on BTC/USD")
        ax.set_ylabel("Equity (growth of $10,000)")
        ax.legend()
        ax.grid(alpha=0.3)
        fig.tight_layout()
        fig.savefig(os.path.join(HERE, "equity_curve.png"), dpi=140)
        print(f"Chart saved: {os.path.join(HERE, 'equity_curve.png')}")
    except ImportError:
        print("(matplotlib not installed - skipping chart)")


if __name__ == "__main__":
    main()
