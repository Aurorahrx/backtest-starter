# Hook copy — community posts for the free starter

These are ready-to-post drafts for distributing the FREE version
(`Backtest in 100 Lines`). Rules: the free thing is the hero; the paid
pack gets at most one sentence at the end; never promise profits.

---

## 1. Reddit — r/algotrading (primary)

**Title:** I built the smallest honest backtest possible: 100 lines, no look-ahead, costs included — free

**Body:**
I keep seeing strategy screenshots with no drawdown column, so I made
the antidote: a single-file Python backtest that bakes in the two rules
most beginners skip — signals from day t apply from day t+1, and every
position change pays 10bps.

It runs on 4.8 years of real BTC daily data (included), prints a full
metric table (return / CAGR / Sharpe / maxDD / vol / exposure), and
compares against buy & hold. One command: `python mini_backtest.py`.

The sample run is interesting: SMA 50/200 beats buy & hold on BTC
(+91% vs +69%, half the drawdown) — but the max drawdown is still -40%,
which is exactly why I'd never sell this as "a strategy."

It's free (link below), no email wall, no API keys. I built it because
someone gave me a backtester for free once and it saved me years.

[free download link]

Edit: to be clear — the script is the point, not the strategy. Change
the fast/slow windows or costs and watch the conclusion flip.

---

## 2. Hacker News — Show HN (primary)

**Title:** Show HN: Backtest in 100 Lines — a no-look-ahead backtester with costs built in

**Body:**
A single-file Python script that runs a SMA 50/200 backtest on bundled
BTC daily data (2022–2026) and prints an honest metric table plus an
equity curve.

Two conventions make it honest by construction:
- positions are applied from the NEXT bar (no look-ahead), and
- transaction costs are charged on every position change.

The point isn't the strategy (which, like most, barely beats buy &
hold after costs in some windows and loses in others) — it's the
discipline. I'd love feedback on the conventions themselves: what
else makes a backtest "honest" that I should add to the paid, full
version I'm building?

Free download, no signup: [link]

---

## 3. V2EX — 分享创造 node (primary)

**标题：** 分享创造：100 行 Python 跑出第一个「诚实」的回测（免费，含 4.8 年 BTC 真实数据）

**正文：**
被各种只有收益截图、没有回撤列的「策略」图刷屏太多，就写了个
反例：一个单文件的 Python 回测脚本，把两条新手最容易忽略的规则
写死在代码里——

1. 信号 t 日收盘产生，t+1 日才持仓（无未来函数）；
2. 每次调仓扣 10 bps 手续费。

自带 2022–2026 年 BTC/USD 真实日线数据，一条命令
`python mini_backtest.py` 输出完整指标表（收益/CAGR/Sharpe/最大回撤
/波动率/持仓时间）并对比买入持有。样本结果是 SMA 50/200 跑赢持有
（+91% vs +69%，回撤减半），但最大回撤仍有 -40%——这正是我不把它
当「策略」卖的原因。

免费下载（无注册、无邮件墙）：[链接]
写这个的初心：当年有人免费送我一个回测器，省了我好几年弯路。

---

## 4. X / Twitter (secondary, after the first two gain traction)

**Thread opener:**
I wrote the smallest honest backtest I could: 100 lines of Python.
- no look-ahead (positions apply next bar)
- costs on every position change
- benchmark vs buy & hold
- real BTC data included

One command, free: [link]

The sample result will annoy both camps: it beats buy & hold AND still
has a -40% drawdown. That tension *is* quant research.

---

## 5. r/quant or r/learnpython (fallback)

Use the r/algotrading draft with the intro reworded for learners:
"teaching myself backtesting and made this tiny honest starter — what
am I still missing?" (Framing as a learner invites corrections, which
drives engagement, and stays well inside self-promo norms.)

---

## Posting rules notes (verify current rules before posting)

- **Reddit:** every sub has its own self-promo ratio (many follow the
  site-wide ~10% guideline). r/algotrading explicitly bans paid-service
  promotion; a free educational tool with source-downloadable code is
  generally fine, but post as a text post with the link inside, not a
  link post, and answer comments.
- **HN Show HN:** must be something you made that people can try; don't
  ask for upvotes; the paid version may be mentioned as context but the
  submission itself must stand alone as free.
- **V2EX 分享创造:** requires substantive content + free deliverable;
  hard-selling a paid product in the same post is against the spirit of
  the node.
- **Timing:** HN/Reddit — Mon–Thu, 08:00–11:00 US Eastern; V2EX —
  weekday evenings 21:00–23:00 CST.

## Conversion mechanics

- Free download page (Gumroad free product) captures email = waitlist
  for the paid pack launch.
- The one-sentence upsell: "If this was useful, the full pack (5
  strategy families + walk-forward + 30 prompts) is at [link]."
- Follow-up email (after launch) sends 1 educational email + 1 launch
  email. Nothing else — the product is the marketing.
