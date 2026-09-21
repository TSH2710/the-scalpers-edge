# The Disciplined Trader Journal — Notion Template Setup Guide

This file is the complete blueprint for building the Notion template sold on Gumroad. Follow the steps below to recreate the 7-page system.

**Estimated build time:** 30-45 minutes

---

## Quick Navigation

1. [Workspace Setup](#step-1-create-the-workspace)
2. [Trade Log Database](#step-2-create-the-trade-log-database)
3. [Pre-Trade Checklist](#step-3-create-the-pre-trade-checklist-page)
4. [R-Multiple Calculator](#step-4-create-the-r-multiple-calculator-page)
5. [Psychology Tracker](#step-5-create-the-psychology-tracker-page)
6. [Weekly Review Dashboard](#step-6-create-the-weekly-review-dashboard)
7. [Wash Sale Tracker](#step-7-create-the-wash-sale-tracker)
8. [Session Performance & Spread Tracker](#step-8-create-the-session-performance--spread-tracker)
9. [Cover Page & Navigation](#step-9-create-the-cover-page)

---

## Step 1: Create the Workspace

1. Open Notion → Create a new page
2. Title: **"The Disciplined Trader Journal"**
3. Add icon: 📊 (or a chart icon)
4. Add cover: dark gradient (use Notion's built-in gradients)

---

## Step 2: Create the Trade Log Database

This is your main database. Every trade you make gets logged here.

1. Type `/database` → select "Table - Full Page"
2. Name it: **"Trade Log"**

### Properties to Add

| Property | Type | Options / Formula |
|----------|------|-------------------|
| Date | Date | — |
| Session | Select | Pre-Market, Open, Mid-Day, Lunch, Power Hour, Close |
| Setup | Select | ORB Breakout, VWAP Pullback, Momentum, Reversal, News Play, Scalp, Other |
| Direction | Select | Long, Short |
| Ticker | Text | — |
| Entry Price | Number | — |
| Exit Price | Number | — |
| Stop Loss | Number | — |
| Position Size | Number | — |
| Commission | Number | — |
| Spread Cost | Number | — |
| Hold Time | Formula | `dateBetween(prop("Exit Time"), prop("Entry Time"), "minutes") + " min"` |
| **P&L** | **Formula** | `prop("Exit Price") * prop("Position Size") - prop("Entry Price") * prop("Position Size") - prop("Commission")` |
| **R-Multiple** | **Formula** | `(prop("Exit Price") - prop("Entry Price")) / (prop("Entry Price") - prop("Stop Loss"))` |
| **Win/Loss** | **Formula** | `if(prop("P&L") > 0, "✅ Win", if(prop("P&L") < 0, "❌ Loss", "➖ Breakeven"))` |
| Emotion | Select | Confident, FOMO, Revenge, Greedy, Fearful, Neutral, Overconfident |
| Rules Followed | Checkbox | — |
| Chart Screenshot | Files & Media | — |
| Notes | Text | — |

**Additional date properties needed for Hold Time formula:**
- Entry Time (Date type)
- Exit Time (Date type)

---

## Step 3: Create the Pre-Trade Checklist Page

1. In the workspace sidebar, click "+" → New Page
2. Name it: **"Pre-Trade Checklist"**
3. Add emoji: 📋

### Content:

```
📋 Daily Pre-Trade Checklist

MARKET CONTEXT
□ What session is it? (Adjust position size accordingly)
□ Is there a news event in the next 30 minutes?
□ What's SPY/QQQ doing? (Above/below VWAP → bias direction)
□ Watchlist clean? (Max 5 tickers, set up night before)

TRADE SETUP
□ Is there a clear, named setup? (ORB, VWAP pullback, etc.)
□ Is risk/reward at least 1:1.5?
□ Do I have a defined stop loss?
□ Have I calculated position size? (1% account risk)
□ Do I have an exit plan? (Target + stop + trail stop rule)

SELF-CHECK
□ Am I in the right headspace? (Rated 7+/10)
□ Have I taken a loss recently? (2 losses = half size, 3 = done)
□ Can I state WHY I'm taking this trade in one sentence?
```

### Add a callout block:

> 💡 **The Rule:** Don't enter a single trade until every box is checked. Takes 90 seconds. Saves hours of losses.

---

## Step 4: Create the R-Multiple Calculator Page

1. New page → Name: **"R-Multiple Calculator"**
2. Add emoji: 📐

### Add a text block:

```
📐 R-Multiple Formula:
R = (Exit Price - Entry Price) / (Entry Price - Stop Loss)

Example:
- Entry: $100, Stop: $98, Target: $104
- Risk per share: $2
- Target hit ($104): R = 2R ✅
- Exit at $102: R = 1R ✅
- Stopped out ($98): R = -1R ❌

Rule of thumb:
- Average R above 1.0 = strategy is profitable
- Below 0.8 = exits need work
- Above 1.5 = your winners are way bigger than your losers
```

### Create database: "R-Multiple Tracker"

| Property | Type | Formula / Notes |
|----------|------|-----------------|
| Date | Date | — |
| Account Size | Number | — |
| Risk per Trade ($) | Number | — |
| Risk per Trade (%) | Formula | `prop("Risk per Trade ($)") / prop("Account Size") * 100` |
| Entry Price | Number | — |
| Stop Loss | Number | — |
| Target Price | Number | — |
| Actual Exit | Number | — |
| **R at Target** | **Formula** | `(prop("Target Price") - prop("Entry Price")) / (prop("Entry Price") - prop("Stop Loss"))` |
| **R at Actual Exit** | **Formula** | `(prop("Actual Exit") - prop("Entry Price")) / (prop("Entry Price") - prop("Stop Loss"))` |
| Win/Loss | Formula | Same as main log |
| Notes | Text | — |

---

## Step 5: Create the Psychology Tracker Page

1. New page → Name: **"Psychology Tracker"**
2. Add emoji: 🧠

### Create database: "Daily Psychology Log"

| Property | Type | Options |
|----------|------|---------|
| Date | Date | — |
| Pre-Trade Mood | Select | Calm, Anxious, Excited, Bored, Angry, Neutral |
| Pre-Trade Energy | Number | 1-10 scale |
| Post-Trade Mood | Select | Same as Pre-Trade |
| FOMO Flag | Checkbox | — |
| Revenge Trading | Checkbox | — |
| Overconfidence | Checkbox | — |
| Fear | Checkbox | — |
| Distraction | Checkbox | — |
| Rule Violation | Checkbox | — |
| Rule Violation Type | Select | No stop, Size too big, Chased entry, Held too long, Other |
| Journal Note | Text | — |

### Add a callout:

> 🚩 **Red Flag Rules:**
> - 3+ revenge trades in a week → mandatory day off
> - FOMO entries consistently losing → wait for pullbacks
> - Overconfidence after wins → stick to position sizing rules
> - Fear exits → set wider stops or use mental stops

---

## Step 6: Create the Weekly Review Dashboard

1. New page → Name: **"Weekly Review"**
2. Add emoji: 📊

### Add heading: "This Week's Stats"

Create a linked database from your main **Trade Log** with filter: Date → This Week.

Add these rollup properties:

| Stat | Rollup / Formula |
|------|------------------|
| Total Trades | Count all entries |
| Wins | Count where Win/Loss = ✅ Win |
| Losses | Count where Win/Loss = ❌ Loss |
| **Win Rate** | Wins / Total Trades |
| **Net P&L** | Sum of P&L |
| **Avg R-Multiple** | Average of R-Multiple |
| Best Setup | Group by Setup → sort by P&L → top |
| Worst Setup | Group by Setup → sort by P&L → bottom |
| Best Session | Group by Session → sort by P&L → top |
| Total Commissions | Sum of Commission |
| Total Spread Cost | Sum of Spread Cost |
| Spread % of Gross | (Spread Cost / Gross Profit) × 100 |

### Add reflection prompt:

```
This Week's Reflection:

What worked:
• Which setups were profitable?
• What time of day did I trade best?
• What was my emotional state during winning trades?

What didn't:
• Which setups lost money?
• Did I break any rules?
• What emotions affected my decisions?

Action items for next week:
□ Eliminate worst-performing setup
□ Increase size on best-performing setup (if R supports it)
□ Stick to pre-trade checklist every trade
□ Avoid trading during [specific time]
```

---

## Step 7: Create the Wash Sale Tracker

1. New page → Name: **"Wash Sale Tracker"**
2. Add emoji: 🧾

### Create database: "Wash Sale Log"

| Property | Type | Formula |
|----------|------|---------|
| Ticker | Title | — |
| Buy Date | Date | — |
| Buy Price | Number | — |
| Sell Date | Date | — |
| Sell Price | Number | — |
| Shares | Number | — |
| **Loss Amount** | **Formula** | `(prop("Buy Price") - prop("Sell Price")) * prop("Shares")` |
| Replacement Buy Date | Date | — |
| Replacement Buy Price | Number | — |
| **Days Until Wash Expires** | **Formula** | `dateBetween(prop("Replacement Buy Date"), prop("Sell Date"), "days")` |
| **Wash Sale Warning** | **Formula** | `if(prop("Replacement Buy Date") and prop("Days Until Wash Expires") < 31, "⚠️ WASH SALE", "✅ OK")` |
| Notes | Text | — |

### Add callout:

> 📋 **Wash Sale Rules:**
> - Can't claim loss if you buy "substantially identical" security within 30 days before/after sale
> - Violations disallow the loss for current year tax purposes
> - Strategy: Wait 31 days before rebuying, or track it and accept the deferral

---

## Step 8: Create the Session Performance & Spread Tracker

1. New page → Name: **"Session Performance"**
2. Add emoji: ⚡

### Create database: "Session Performance"

| Property | Type | Options |
|----------|------|---------|
| Session | Select | First 30 Min, 10AM-11AM, Lunch, Mid-Afternoon, Power Hour, Last 30 Min |
| Date | Date | — |
| Trades | Rollup (from Trade Log) | Count |
| Win Rate | Rollup | Average |
| Avg Hold Time | Rollup | Average |
| Avg P&L | Rollup | Average |
| Net P&L | Rollup | Sum |
| Avg Spread Cost | Rollup | Average |
| Commissions | Rollup | Sum |

### Add spread tracker table (manual entry is fine):

```
Session Spread Tracker:

| Session | Avg Spread/Trade | Total Spread | Spread % of Gross |
|---------|-----------------|--------------|-------------------|
| First 30 Min |               |              |                   |
| 10AM-11AM |               |              |                   |
| Lunch |               |              |                   |
| Mid-Afternoon |               |              |                   |
| Power Hour |               |              |                   |
| Last 30 Min |               |              |                   |

Goal: Keep spread costs below 15% of gross profit.

If above 15%:
• Trade more liquid stocks
• Use limit orders
• Reduce trade frequency
```

### Add callout:

> 💰 **Spread Cost Per Trade Formula:**
> `(Ask - Bid at entry + Ask - Bid at exit) × Position Size`
>
> A $0.05 spread on 200 shares = $20 per trade. That's $100/week if you trade 5x/day.
> Over 50 weeks: $5,000. Track it.

---

## Step 9: Create the Cover Page

1. Go to the top-level page (the parent page you created in Step 1)
2. Add heading: **"The Disciplined Trader Journal"**
3. Add a callout:

```
📊 Your complete scalping journal — track trades, monitor psychology, and review performance.

Start here:
1. Open "Pre-Trade Checklist" before each session
2. Log every trade in "Trade Log"
3. Review weekly with "Weekly Review Dashboard"

Pages:
→ Pre-Trade Checklist
→ Trade Log (main database)
→ R-Multiple Calculator
→ Psychology Tracker
→ Weekly Review Dashboard
→ Wash Sale Tracker
→ Session Performance & Spread Tracker
```

4. Type `/toc` to add a table of contents

---

## Making It a Template

Once all 7 pages are built:

1. Click "..." on the top-level page
2. Select **"Turn into template"**
3. Add description: *"The Disciplined Trader Journal — a Notion trade journal built specifically for scalpers. 7 pages with pre-built formulas. Duplicate and start logging in 2 minutes."*
4. Add preview screenshots of each page (dark theme recommended)
5. Optionally publish to the Notion Template Gallery for extra visibility

## Screenshots to Capture for Marketing

Take these screenshots for your Gumroad listing and landing page (use Notion's dark theme):

1. Cover page / table of contents
2. Trade Log (filled with sample data — see sample-data.md)
3. R-Multiple Calculator (showing formulas)
4. Psychology Tracker dashboard
5. Weekly Review Dashboard (with stats)
6. Wash Sale Tracker
7. Session Performance heatmap
8. Pre-Trade Checklist page
