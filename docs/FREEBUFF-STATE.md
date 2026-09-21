# The Scalper's Edge — Project State

**Last updated:** September 20, 2026
**Owner:** Tristan (TSH2710)
**Status:** Launch active, building audience

---

## 🎯 Project Overview

A Notion trade journal template built specifically for scalpers. Sold on Gumroad as a one-time purchase ($49) with a free Lite version as a lead magnet.

**Core product:** The Disciplined Trader Journal ($49)
**Lead magnet:** Lite version (free, daily trade log + R-calc)

---

## 🔗 Live Links

**Main site:** https://scalpers-edge.netlify.app
**Gumroad store:** https://tinkshifter.gumroad.com
**$49 product:** https://tinkshifter.gumroad.com/l/disciplined-trader-journal
**Free Lite:** https://tinkshifter.gumroad.com/l/inqxzl

**X (Twitter):** https://x.com/Scalpersedge
**Instagram:** https://www.instagram.com/scalpersedge_official

**Blog:** https://scalpers-edge.netlify.app/blog/index.html

---

## ✅ Completed Tasks

### Store Setup
- [x] Gumroad products created ($49 + Free Lite)
- [x] LAUNCH20 discount code (20% off, 25 uses)
- [x] Cross-sell from Lite → $49 at checkout
- [x] 14-day refund policy set on both products
- [x] Custom landing pages for both products
- [x] Product thumbnails/screenshots (8 PNG files)

### Website
- [x] Main site deployed on Netlify
- [x] 8 blog posts (honest, no fabricated claims)
- [x] Share cards (OG images) for all pages
- [x] Social links (X + Instagram) on all pages
- [x] Free Lite links added to website
- [x] Email capture section for Lite
- [x] Privacy/Terms pages

### Social Media
- [x] X account created (@Scalpersedge)
- [x] X profile setup (avatar, banner, bio)
- [x] Launch tweet posted with trade-log screenshot
- [x] Instagram account created (@scipersedge_official)
- [x] Instagram profile setup (avatar, bio, link in bio)
- [x] 2 Instagram posts live

### Content
- [x] 80+ Twitter posts in content bank (`social-content/twitter-ongoing.md`)
- [x] Reddit strategy guide (`social-content/reddit-strategy.md`)
- [x] X account setup kit (`social-content/x-account-setup.md`)
- [x] Email sequence drafted (`gumroad/lite-email-sequence.md`)
- [x] Product listing copy (`gumroad/product-listing.md`)

### Automation
- [x] Tomorrow's posts scheduled (8 AM & 12 PM via Task Scheduler)
- [x] Pushover notifications configured
- [x] Email workflow created (but needs $100 to publish)

---

## ⏳ Pending Tasks

### High Priority
- [ ] Pin launch tweet on X (manual - Tristan)
- [ ] Start daily X reply routine (20 min/day)
- [ ] Record 45-second tour video
- [ ] Connect bank account in Gumroad (with dad)

### Medium Priority
- [ ] Publish email workflow (needs $100 earnings)
- [ ] Register thescalpersedge.com domain
- [ ] Set up Netlify DNS for custom domain
- [ ] Post to Reddit (r/Daytrading, r/Trading)

### Low Priority
- [ ] Create TikTok account
- [ ] YouTube channel for tutorial videos
- [ ] LinkedIn presence

---

## 📊 Automation Status

### Scheduled Posts (Task Scheduler)
- **8 AM daily:** Spread costs tweet
- **12 PM daily:** R-multiples tweet
- **Setup:** `tools/run-post.py` with Pushover notifications

### Pushover Config
- User Key: `u4s6xys1bvkjbp5du36whquyh1onjk`
- App Token: `ashtu2j2fkmfwik6svgux6ujrydkoh`
- Status: ✅ Working

### Email Workflow
- Name: "Lite to Full Journal Sequence"
- Trigger: Purchase of Lite product
- Status: ⚠️ Saved but unpublished (needs $100)
- Emails: 3 (immediate, 3 days, 10 days)

---

## 📁 Project Structure

```
scalpers-edge/
├── index.html                    # Main site
├── blog/                         # 8 blog posts + index
├── og/                           # Share cards (PNG)
├── gumroad/
│   ├── landing/                  # Landing pages
│   │   ├── landing-v3.html       # $49 page
│   │   └── landing-lite.html     # Free Lite page
│   ├── lite-email-sequence.md    # Email workflow content
│   └── product-listing.md        # Product copy
├── social-content/
│   ├── assets/                   # Avatar, banner PNGs
│   ├── x-account-setup.md        # X setup guide
│   ├── twitter-ongoing.md        # 80+ tweet ideas
│   └── reddit-strategy.md        # Reddit posting guide
├── tools/
│   ├── build_blog.py             # Blog generator
│   ├── build_og_cards.py         # Share card generator
│   ├── run-post.py               # Scheduled posting
│   └── check_site.py             # Site validator
├── _redirects                    # Netlify redirects
├── FREEBUFF-STATE.md             # This file
└── GUMROAD-WORKFLOW-GUIDE.md    # Workflow setup guide
```

---

## 💡 Key Decisions

### Content Strategy
- **Honesty first:** No fabricated P&L numbers, no fake testimonials
- **Teaching > selling:** Blog posts teach, product sells itself
- **Free → Paid funnel:** Lite captures leads, cross-sell converts

### Social Strategy
- **X:** 2-3 posts/day + 5-10 replies on trading accounts
- **Instagram:** 1 post/day with screenshots
- **Reddit:** 1 value-first post/week in trading subs
- **No buying followers, no follow/unfollow, no DM blasts**

### Pricing
- **$49 one-time:** No subscription, lifetime updates
- **LAUNCH20:** 20% off, capped at 25 uses (honest scarcity)
- **14-day refund:** No hoops, instant on request

---

## 🎬 Content Bank

### Twitter Posts (`social-content/twitter-ongoing.md`)
- 80+ ready-to-post tweets
- Mix of: tips, polls, threads, engagement posts
- Avoid: Specific P&L numbers as personal history

### Blog Posts (`blog/`)
1. Why Scalpers Skip Journaling
2. Pre-Trade Checklist
3. R-Multiples Explained
4. Revenge Trading
5. Wash Sales for Day Traders
6. Scalping Psychology (10 AM)
7. Spread Costs Killing Profitability
8. First Year of Scalping

### Instagram Posts
- Post 1: Trade log screenshot + features
- Post 2: Pre-trade checklist + journaling value

---

## 🔧 OpenCLI Commands

### Twitter
```bash
opencli twitter post "text" --images "path.png" --window background -f yaml
opencli twitter whoami -f yaml
opencli twitter tweets Scalpersedge -f yaml
```

### Instagram
```bash
opencli instagram post "caption" --media "path.png" --window background -f yaml
opencli instagram whoami -f yaml
```

### Browser Automation
```bash
opencli browser <session> open <url>
opencli browser <session> state
opencli browser <session> screenshot /tmp/file.png
opencli browser <session> eval "javascript"
```

---

## 📈 Success Metrics (When to Celebrate)

- [ ] First sale (any amount)
- [ ] 10 free Lite downloads
- [ ] 100 X followers
- [ ] 100 Instagram followers
- [ ] $100 earnings (unlocks email workflow)
- [ ] First organic blog visitor (via SEO)

---

## 🚨 Known Issues

1. **thescalpersedge.com not registered** — domain doesn't exist yet
2. **Email workflow unpublished** — needs $100 earnings
3. **Bank not connected** — sales accumulate in Gumroad balance
4. **Push token in git remote** — should rotate later

---

## 📝 Notes for Next Session

- User is a student — available after school
- Trades XAU/USD on Hankotrade
- Uses TradingView for charts
- Learning to automate social posting
- Focus on building audience before scaling sales

---

**Generated by Freebuff 🤖**
**Co-Authored-By: Codebuff <noreply@codebuff.com>**
