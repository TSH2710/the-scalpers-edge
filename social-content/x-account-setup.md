# @scalpersedge — X Account Setup Kit

Everything needed to stand up the X account in ~10 minutes. Assets are in
`social-content/assets/`. Content below replaces the fabricated-stats drafts
in `twitter-launch.md` with honest versions (this store has real buyers now,
but no beta cohort — don't invent numbers).

---

## 1. Setup checklist (do in this order)

- [ ] Sign up at x.com with a dedicated email → handle: **@scalpersedge**
      (if taken: `@scalpersedge_`, `@thescalpersedge`, `@scalpersedgehq` — in that order)
- [ ] Profile photo → `social-content/assets/avatar-400.png`
- [ ] Banner → `social-content/assets/banner-1500x500.png`
- [ ] Name → **The Scalper's Edge**
- [ ] Bio → (below, ≤160 chars)
- [ ] Location field → `tinkshifter.gumroad.com` (acts as the link line until the custom domain is live)
- [ ] Post the pinned tweet (below), then pin it
- [ ] Fix site links (see §5) so bio links don't 404
- [ ] Follow 20–30 scalping/trading accounts; reply (don't DM) with useful comments

**Bio (159 chars, fits):**

```
Trade smarter. Journal harder.

Notion trade journal built for scalpers — R-multiples, spread costs, session heatmaps, psychology flags.

Free lite + full template ↓
```

---

## 2. Pinned post (the launch post)

```
I scalped for a year before I journaled a single trade.

Winged it, repeated the same mistakes, blamed "the market."

Built the journal I wish I'd had on day 1:

• 12-pt pre-trade checklist
• auto P&L + R-multiples
• spread cost tracking
• psychology flags (FOMO / revenge)
• session heatmaps

Duplicate to Notion in 2 min ↓
https://tinkshifter.gumroad.com/l/disciplined-trader-journal
```

Attach as image: a screenshot of the **daily trade log page** (use
`gumroad/landing/screenshots/trade-log.png`). Screenshots outperform text.

---

## 3. First week of posts (honest versions)

**Launch-week offer (real, verifiable):** the first 25 buyers get 20% off
with code **LAUNCH20** at checkout — the cap is set in Gumroad, so the
claim can never overpromise. Mention it in the Day 1 and Day 3 posts and
then let it expire quietly when the 25 are gone.

These follow the cadence from `twitter-launch.md` but strip invented beta
stats. Post 2–3/day; engagement beats volume early on.

**Day 1 — problem post**

```
Most scalpers don't journal. Not because they're lazy.

Because every tool they try was built for someone holding AAPL for 3 months.

5-20 trades a day needs: spread tracking, session stats, R-multiples, and a checklist that catches FOMO before the entry.

Not another generic spreadsheet.
```

**Day 1 — what shipped**

```
Spent the last month building a Notion trade journal specifically for scalpers.

7 pages, all formulas pre-wired. Duplicate and start logging today.

Free lite version (daily log + R-calc) if you want to try before buying:

https://tinkshifter.gumroad.com/l/inqxzl
```

**Day 2 — spread costs**

```
Spread costs kill more scalpers than bad entries.

$0.02 spread × 500 shares = $10 per round trip.

10 trades/day = $100/day gone before you're right or wrong about anything.

If you're not tracking it separately, you don't know your real edge.
```

**Day 3 — R-multiples**

```
R-multiple reminder:

You can be profitable at a 40% win rate with 1.5R average.
You can blow up at a 70% win rate with 0.4R average.

Win rate is a vanity metric. Average R is the number.

Your journal should compute it for you.
```

**Day 4 — psychology**

```
"I just need to control my emotions."

Cool. How?

You can't control what you don't measure.

Log emotional state after every trade for 2 weeks. The pattern (mine was: revenge trades after a morning loss) is worth more than any $500 course.
```

**Day 5 — the honest build-in-public**

```
Launch numbers, week 1 — the honest version:

• store is live, first real sales coming in
• zero budget, zero followers
• shipping every fix buyers ask for in public

Follow along if you're building something too.
```

**Day 6 — poll**

```
Quick poll for scalpers: what's actually costing you money right now?

A) FOMO entries
B) Revenge trading after a loss
C) Trading dead sessions
D) No idea — that's the problem
```

**Day 7 — the free lite**

```
Not ready to pay for a journal? Fair.

The lite version is free: daily trade log + R-multiple calculator. No card, no catch.

Duplicate it, run it for a week, and you'll see what a week of real data feels like.

https://tinkshifter.gumroad.com/l/inqxzl
```

---

## 4. Ongoing engine

`social-content/twitter-ongoing.md` has 80+ ready posts (tips, polls, thread
starters). They're fine as-is — the only ones to avoid are the six that cite
specific revenue/win-rate numbers as personal history until you have them.
Rule of thumb: **never post a number you didn't pull from your own journal.**

Weekly rhythm: Mon reflection · Wed tip · Fri week-in-review · 1 thread/week.
Reply strategy: 5–10 thoughtful replies/day on mid-size trading accounts.

---

## 5. Link routing (redirects built, domain pending)

The repo has a Netlify `_redirects` file ready for when the domain is
registered and pointed at Netlify:

- `thescalpersedge.com/journal` → Gumroad ($49 Journal)
- `thescalpersedge.com/lite` → Gumroad (free Lite)

These are live once the `_redirects` file is deployed with the site
(git push / Netlify deploy). The blog posts already link to `/journal`, so
they start working the moment it ships. Social posts should use the clean
domain URLs — they're shorter, branded, and re-targetable later (302).

---

## 6. Assets

| File | Use |
|---|---|
| `assets/avatar-400.png` | Profile photo (400×400) |
| `assets/banner-1500x500.png` | Banner (1500×500, lockup inside safe area) |
| `assets/avatar.svg` / `assets/banner.svg` | Editable sources |
| `assets/x-profile-preview.html` | Open in browser to preview the profile |
