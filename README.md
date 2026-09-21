# The Scalper's Edge

Notion trade journal for scalpers. Sold on Gumroad with a free Lite version as a lead magnet.

## 🚀 Quick Start

**Main Site:** https://scalpers-edge.netlify.app
**Gumroad:** https://tinkshifter.gumroad.com
**X:** @Scalpersedge
**Instagram:** @scipersedge_official

## 📁 Project Structure

```
scalpers-edge/
├── 📄 index.html                    # Main site (Netlify root)
├── 📄 privacy.html                  # Privacy policy
├── 📄 terms.html                    # Terms of service
├── 📄 404.html                      # Custom 404 page
├── 📄 robots.txt                    # SEO robots
├── 📄 sitemap.xml                   # SEO sitemap
├── 📄 _redirects                    # Netlify redirects
│
├── 📁 blog/                         # 8 blog posts
│   ├── index.html                   # Blog index
│   └── *.html                       # Individual posts
│
├── 📁 gumroad/                      # Gumroad assets
│   ├── landing/                     # Landing pages
│   └── *.md                         # Product docs
│
├── 📁 social-content/               # Social media assets
│   ├── assets/                      # Avatars, banners
│   └── *.md                         # Content guides
│
├── 📁 og/                           # Share cards (PNG)
│
├── 📁 tools/                        # Build scripts
│   ├── build_blog.py                # Blog generator
│   ├── build_og_cards.py            # Share card generator
│   ├── run-post.py                  # Scheduled posting
│   └── check_site.py                # Site validator
│
├── 📁 docs/                         # 📚 Documentation
│   ├── FREEBUFF-STATE.md            # Project state for AI
│   ├── changelog.md                 # What changed
│   ├── decisions.md                 # Why we did things
│   └── milestones.md                # Progress tracking
│
├── 📁 history/                      # 📜 Project timeline
│   ├── changelog.md                 # Version history
│   ├── decisions.md                 # Key decisions
│   └── milestones.md                # Achievements
│
├── 📁 agents/                       # 🤖 AI agent configs
│   ├── prompts/                     # Reusable prompts
│   └── skills/                      # Custom skills
│
├── 📁 skills/                       # 🎯 Reusable skills
│   ├── posting/                     # Social posting
│   ├── automation/                  # Workflow automation
│   └── content/                     # Content generation
│
├── 📁 plugins/                      # 🔌 Integrations
│   ├── gumroad/                     # Gumroad API
│   ├── opencli/                     # OpenCLI adapters
│   └── netlify/                     # Netlify config
│
├── 📁 automation/                   # ⚙️ Automated workflows
│   ├── scheduled-posts/             # Task Scheduler
│   ├── email-workflows/             # Gumroad emails
│   └── notifications/               # Pushover setup
│
├── 📁 content/                      # 📝 Content bank
│   ├── twitter/                     # Tweet drafts
│   ├── instagram/                   # Post drafts
│   ├── reddit/                      # Reddit drafts
│   ├── blog/                        # Blog drafts
│   └── email/                       # Email templates
│
├── 📁 assets/                       # 🎨 Media files
│   ├── images/                      # Screenshots
│   ├── videos/                      # Video files
│   ├── design/                      # SVGs, designs
│   └── brand/                       # Logos, avatars
│
├── 📁 config/                       # ⚙️ Configuration
│   ├── settings.md                  # Project settings
│   └── credentials.md               # API keys (gitignored)
│
├── 📁 templates/                    # 📋 Reusable templates
│   ├── notion/                      # Notion templates
│   ├── landing/                     # Landing pages
│   └── emails/                      # Email templates
│
├── 📁 research/                     # 🔍 Market research
│   ├── competitors/                 # Competitor analysis
│   ├── audience/                    # Target audience
│   └── trends/                      # Market trends
│
├── 📁 analytics/                    # 📊 Performance
│   ├── metrics.md                   # Key metrics
│   └── reports/                     # Weekly reports
│
├── 📁 projects/                     # 🚀 Active projects
│   └── README.md                    # Projects overview
│
├── 📁 backups/                      # 💾 Safety net
│   ├── pre-launch/                  # Pre-launch backup
│   └── critical/                    # Critical files
│
├── 📁 drafts/                       # 📝 Work in progress
│   ├── content/                     # Draft posts
│   ├── code/                        # Draft scripts
│   └── ideas/                       # Idea backlog
│
└── 📁 _archive/                     # 🗄️ Old files
    ├── old-versions/                # Previous versions
    └── deprecated/                  # No longer used
```

## 🎯 Current Status

**Phase:** Launch Active
**Focus:** Building audience, getting first sales
**Revenue:** $0 (building toward $100)

### ✅ Done
- Website live on Netlify
- 8 blog posts published
- Gumroad store armed (LAUNCH20, cross-sell)
- X account launched (@Scalpersedge)
- Instagram account launched (@scipersedge_official)
- Automated posting scheduled

### ⏳ Next
- Pin launch tweet
- Start daily X routine
- Record tour video
- Connect bank account
- Hit first sale

## 🔗 Quick Links

**Buy:** https://tinkshifter.gumroad.com/l/disciplined-trader-journal
**Free:** https://tinkshifter.gumroad.com/l/inqxzl
**Blog:** https://scalpers-edge.netlify.app/blog/
**X:** https://x.com/Scalpersedge
**Instagram:** https://www.instagram.com/scalpersedge_official

## 📚 Documentation

- [Project State](docs/FREEBUFF-STATE.md) — AI agent context
- [Changelog](history/changelog.md) — What changed
- [Decisions](history/decisions.md) — Why we did things
- [Milestones](history/milestones.md) — Progress tracking
- [Settings](config/settings.md) — Project config

## 🛠️ Development

```bash
# Build blog
python tools/build_blog.py

# Generate share cards
python tools/build_og_cards.py

# Check site
python tools/check_site.py

# Post to X
opencli twitter post "text" --window background -f yaml

# Post to Instagram
opencli instagram post "caption" --window background -f yaml
```

## 📊 Success Metrics

| Metric | Target | Status |
|--------|--------|--------|
| X Followers | 100 | 🟡 In Progress |
| Instagram Followers | 100 | 🟡 In Progress |
| Free Lite Downloads | 10 | 🟡 In Progress |
| Paid Sales | 1 | 🟡 In Progress |
| Revenue | $100 | 🟡 In Progress |

---

**Built by Tristan, for scalpers.**
**Generated with Codebuff 🤖**
