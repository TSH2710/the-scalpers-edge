# Spread Costs Are Killing Your Profitability — Here's How to Track Them

*You're tracking P&L. You're tracking win rate. But you're missing the single biggest drain on your account. Here's what spread costs are costing you — and how to stop it.*

---

I made $1,200 in gross profit in my first full month of scalping.

Sounds good, right? Until I broke down the numbers:

- Gross profit: $1,200
- Commissions: $89
- Spread costs: $347

**Net profit: $764**

That's right. 29% of my gross profit disappeared in the spread. I was paying nearly a third of my profits to liquidity providers and I didn't even realize it.

Today I'm going to show you exactly what spread costs are, why they're invisible, and how tracking them transformed my profitability.

## What Is the Spread?

The spread is the difference between the bid (what buyers will pay) and the ask (what sellers want).

**Example:**
- Bid: $10.00
- Ask: $10.05
- Spread: $0.05 (5 cents per share)

When you buy at the ask and immediately sell at the bid, you lose the spread. That 5 cents is gone. It's not a commission — it's the cost of entering and exiting the market.

For scalpers who hold for seconds to minutes, the spread is EVERYTHING.

## Why Spread Costs Are Invisible

Your brokerage statement shows commissions. It shows fees. It shows everything except the spread.

Why? Because the spread is embedded in your execution price. You see $10.05 as your buy price and $10.10 as your sell price. You think you made 5 cents per share.

But if the "true" price was $10.025 (midpoint), you paid $0.025 to enter and $0.075 to exit. Total spread cost: $0.10 per share.

On 200 shares, that's $20. Invisible. Unreported. And absolutely devastating over time.

## The Numbers: What Spread Costs Actually Look Like

I tracked my spread costs for 4 weeks. Here's what I found:

| Week | Gross Profit | Spread Costs | % of Gross | Net Profit |
|------|-------------|--------------|------------|------------|
| 1 | $1,200 | $347 | 29% | $853 |
| 2 | $980 | $89 | 9% | $891 |
| 3 | $1,450 | $412 | 28% | $1,038 |
| 4 | $720 | $156 | 22% | $564 |

Week 2 was different. I'd switched from low-liquidity names (average spread: $0.08) to high-liquidity names (average spread: $0.02).

Same trading strategy. Same number of trades. Different stock selection = 20% difference in profitability.

## How to Calculate Your Spread Cost Per Trade

Here's the formula:

```
Spread cost per share = (Ask - Bid) at entry + (Ask - Bid) at exit
Total spread cost = Spread cost per share × Shares × 2 (round trip)
```

**Example:**
- Entry: Buy 200 shares at $10.05 (ask), bid is $10.00
- Exit: Sell at $10.10 (bid), ask is $10.15
- Entry spread: $0.05 × 200 = $10
- Exit spread: $0.05 × 200 = $10
- Total spread cost: $20

But wait — you also "paid" the spread on entry. Your effective entry was $10.025 (the midpoint). Your effective exit was $10.125. So your real P&L is $0.10/share, not $0.05/share.

The spread cost on this trade is $10 (half on entry, half on exit).

## How to Track It in Your Journal

I added a spread tracker to my journal. Every trade logs:

1. **Entry spread** (ask - bid at time of entry)
2. **Exit spread** (ask - bid at time of exit)
3. **Total spread cost** (entry + exit × shares)
4. **Spread as % of gross P&L**

Here's the weekly breakdown from my journal:

| Week | Avg Spread/Trade | Total Spread Cost | Spread % of Gross | Trades |
|------|-----------------|------------------|-------------------|--------|
| 1 | $28.50 | $427 | 29% | 15 |
| 2 | $8.90 | $134 | 9% | 15 |
| 3 | $31.20 | $468 | 30% | 15 |
| 4 | $15.60 | $234 | 22% | 15 |

The pattern is obvious: my spread cost is entirely determined by which stocks I trade, not how I trade them.

## How to Reduce Spread Costs

### 1. Trade Higher-Liquidity Stocks

This is the single biggest lever.

**Low-liquidity names (spread: $0.05-$0.15):**
- Penny stocks under $5
- Low-volume small caps
- Stocks with <500K daily volume

**High-liquidity names (spread: $0.01-$0.03):**
- SPY, QQQ, AAPL, MSFT, NVDA, TSLA
- Stocks with >5M daily volume
- Large-cap S&P 500 names

Switching from low-liquidity to high-liquidity names cut my spread costs by 70%.

### 2. Use Limit Orders (When It Makes Sense)

Market orders pay the spread. Limit orders don't — but they might not fill.

The compromise:
- **Entry:** Use a limit order at the midpoint or better
- **Exit:** Use a limit order at your target, not a market order

This is especially effective for larger positions where the spread compounds quickly.

### 3. Trade at Optimal Times

The spread widens at:
- Market open (9:30-9:45): Highest volatility, widest spreads
- Market close (3:55-4:00): Everyone rushing to exit
- News events: Uncertainty widens spreads

The spread is narrowest mid-session (10:30AM-2:30PM). If you're trading wide-spread names, this is your window.

### 4. Increase Your Position Size (Carefully)

This sounds counterintuitive, but hear me out.

If your spread is $0.05 per share:
- 100 shares = $5 round trip
- 200 shares = $10 round trip
- 500 shares = $25 round trip

But if your average profit per trade is $50, the $5 spread on 100 shares is 10% of your gross profit. The $10 spread on 200 shares is only 5%.

Bigger positions dilute the spread as a percentage of your profit.

**CAUTION:** Only do this if your risk management scales with it. More shares = more risk. Calculate your position size using your 1% risk rule, not the other way around.

### 5. Avoid Low-Price Stocks

A $0.05 spread on a $2 stock is 2.5%. The same $0.05 spread on a $200 stock is 0.025%.

For scalpers, percentage spread matters more than absolute spread. A 2% spread on a $2 stock means you need a 2% move just to break even.

Stick to stocks above $15. Above $50 if you can. The spread percentage becomes negligible.

## The Spread Impact on Different Strategies

Not all strategies are equally affected by spreads:

| Strategy | Avg Hold Time | Spread Impact | Mitigation |
|----------|---------------|---------------|------------|
| Day scalping (seconds-minutes) | Very High | Trade high-liquidity only | Limit orders, optimal timing |
| Day trading (minutes-hours) | High | Significant | Stock selection, limit entries |
| Swing trading (days-weeks) | Medium | Minimal | Less important |
| Position trading (months) | Low | Negligible | Irrelevant |

If you're a scalper, spread IS the cost of doing business. You can't eliminate it — but you CAN minimize it.

## What My Spread Tracker Looks Like

I built a spread tracking page into The Disciplined Trader Journal. Every trade auto-logs:

- Average spread per trade
- Total spread cost (daily/weekly/monthly)
- Spread as percentage of gross profit
- Spread by ticker (which stocks are costing you most)
- Spread by session (when are spreads widest)

After 4 weeks, I had a clear picture: I was trading too many low-liquidity names in the first 30 minutes. The combination was brutal.

**The fix:**
1. First 30 minutes: only trade SPY/QQQ/AAPL (tight spreads)
2. After 10AM: expand watchlist to include higher-liquidity mid-caps
3. Avoid anything under $15 or under 1M daily volume
4. Result: spread costs dropped from 29% of gross to 9%

That 20% difference funded my subscription to the journal template (and then some).

## Common Objections

**"Spread costs are just part of trading."**
True. But they're not supposed to be 30% of your profits. That's not "the cost of doing business" — that's bad stock selection.

**"I focus on big movers, not spreads."**
The biggest movers often have the widest spreads. Low-volume stocks gap more, but you pay for that volatility in the spread.

**"My broker gives me rebates for high volume."**
Maybe. But rebates on a $0.08 spread don't make it a $0.02 spread. Find the stocks with the tightest spreads first, then optimize execution.

## The Bottom Line

You wouldn't drive to work every day without knowing your gas mileage. So why trade without knowing your spread cost?

Here's what to do this week:
1. Add spread tracking to your journal
2. Log every trade with entry/exit bid-ask spreads
3. Calculate total spread cost at the end of each day
4. Compare: which stocks/times are costing you most?
5. Eliminate the worst offenders

I went from 29% of gross profit to 9% just by switching from low-liquidity to high-liquidity names.

That's $200+ per month in recovered profit. From a single change to my stock selection.

Track your spreads. Fix your stock list. Keep more of what you earn.

---

**P.S.** The Disciplined Trader Journal has automatic spread tracking built in. Log your entry and exit prices, and it calculates your real spread cost alongside your R-multiple. See exactly where your money is going. [Get it here for $49](https://thescalpersedge.com/journal).

**P.P.S.** What's your spread cost as a percentage of gross profit? Drop it in the comments. I bet it's higher than you think.

---

*About the author: I'm a scalper with ~1 year of experience. I once lost 29% of my gross profit to spreads before I started tracking them. Now I keep most of what I earn. Follow along at [@scalpersedge](https://x.com/scalpersedge) on Twitter.*
