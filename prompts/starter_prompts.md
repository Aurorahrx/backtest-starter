# Starter Prompts: 10 free prompts to generate your first testable ideas

Free sampler from the Quant Research Template Pack (which contains 30
full-length prompts across the entire research loop). Fill the
`{placeholders}` and paste into any LLM.

---

**1. The idea engine**
> I trade `{market}` on a `{timeframe}` horizon. I believe price moves are
> driven by `{mechanism}`. Give me 5 testable trading hypotheses based on
> this mechanism. For each: exact entry/exit rule, why the edge should
> persist, and the one condition under which it should fail.

**2. The devil's advocate**
> My trading hypothesis is: `{hypothesis}`. Argue against it as hard as
> possible — structural changes, crowding, costs, data artifacts. Which
> of your objections can a backtest detect, and which can it not?

**3. The cost reality check**
> My strategy trades `{instrument}` about `{N}` times/year at `{position
> size}`. Break down realistic all-in costs per round trip (commission,
> spread, slippage, funding) and tell me how much each extra basis point
> reduces my annual return.

**4. The look-ahead audit**
> Here is my signal code: `{paste}`. Find every place future data leaks
> into the signal, every shift/ffill mistake, and every silently dropped
> NaN. Quote the exact lines and give the fix.

**5. The benchmark question**
> I will judge my strategy against `{benchmark}`. Propose 3 benchmarks
> that are stricter, and tell me which one makes it hardest for a
> mediocre strategy to pass.

**6. The overfitting confession**
> I tried `{K}` parameter combinations and the best had Sharpe `{S}`.
> With `{K}` trials, what Sharpe would pure luck produce? What haircut
> should I apply to my reported number? Show the math.

**7. The walk-forward reader**
> Here are my walk-forward folds (is_sharpe, oos_sharpe per fold):
> `{paste}`. Is the out-of-sample performance believable? Is my
> parameter choice stable across folds? What single follow-up test
> would you run?

**8. The trade autopsy**
> Here are my per-trade returns: `{paste}`. Are the losses single
> events, regime clusters, or evenly spread? What does the pattern say
> about the strategy's real risk?

**9. The worst-case walk**
> With Sharpe `{S}`, vol `{V}` and max drawdown `{D}`, describe the
> worst realistic losing streak for a `{$size}` account — dates,
> amounts, and how long until a new high. Make it concrete enough to
> scare me.

**10. The go/no-go memo**
> Given `{results summary}`, write a go/no-go memo: the three conditions
> that must all hold before I allocate real capital, my score on each
> today, and the kill criteria I would use live. End with one word:
> GO or NO-GO.

---

The full pack adds 20 more prompts: hypothesis stress-tests, code
generation and review, multiple-testing math, regime splits,
pre-registration contracts, and result writeups — plus the toolkit to
run the tests these prompts ask for.
