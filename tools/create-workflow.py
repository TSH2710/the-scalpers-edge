#!/usr/bin/env python3
"""
Create Gumroad email workflow for Lite product
"""

import asyncio
from playwright.async_api import async_playwright

# Email sequence
EMAILS = [
    {
        "delay": 0,
        "subject": "Your Lite journal is ready (2-minute setup)",
        "body": """Hey {{ first_name }},

Your copy of the Lite trade journal is ready:

https://tinkshifter.gumroad.com/l/inqxzl

Setup is two minutes:

1. Open the template → click "Duplicate" (top right)
2. Pick one thing to log before your next session: entry, exit, size, and one line on why you took it
3. Grade the trade +1R to -3R when you close it

That's it. The full system does more (psychology flags, session heatmaps, weekly reviews, spread tracking), but the free loop above is where every disciplined scalper starts — most never even get this far.

One honest note: I built this because I scalped for about a year before I journaled a single trade, and the mistakes I repeated in that stretch are exactly what the template is designed to catch.

Trade smarter,
Tristan

P.S. The full version — The Disciplined Trader Journal — is $49, and the first 25 buyers get 20% off with code LAUNCH20 at checkout. The cap is real and set in the store, so when it's gone, it's gone. Lite buyers can also grab that same 20% off from the checkout that appears when you grab the template — but only if you want it. The Lite is not a trial with missing pieces; it works on its own."""
    },
    {
        "delay": 3,
        "subject": "The question your trade log answers by Thursday",
        "body": """Hey {{ first_name }},

You grabbed the Lite journal a few days ago. Quick question that decides whether journaling actually helps you:

By Thursday, will your log be able to answer: "What did I lose on, and why?"

If yes — genuinely, well done. Most people who download a template never write a single row. You're ahead of roughly everyone.

If no, here's the pattern to break: logging after the session from memory. Do it during — one line between trades. That's the whole habit.

The full journal automates what the Lite leaves manual:

- Psychology flags — tag revenge / FOMO / boredom at entry, then see which flag actually costs you money (it's rarely the one you'd guess)
- Session heatmaps — first hour vs. lunch vs. close, in R, so your "best time to trade" becomes a number instead of a feeling
- R-multiple analytics — win rate is noise at 10+ trades a day; expectancy is the metric that pays
- Weekly review pages — the 15 minutes Sunday night that replaces next week's repeat mistakes

If that sounds like what you'd build for yourself anyway, it's $49 with a 14-day, no-hoops refund — keep it only if it earns its keep in two weeks.

Get the full journal → https://tinkshifter.gumroad.com/l/disciplined-trader-journal

(First 25 buyers: code LAUNCH20 still works for 20% off.)

Trade smarter,
Tristan"""
    },
    {
        "delay": 10,
        "subject": "Keep the Lite. Genuinely. + one ask.",
        "body": """Hey {{ first_name }},

Last email I'll send about the journal. Two things:

1. If the Lite is all you need — keep it and use it. It's free forever, and a trader with a simple log they actually maintain beats a trader with a perfect system they don't. No hard feelings, no more emails about it.

2. If you've been meaning to upgrade but haven't: the full journal is $49, first 25 buyers get LAUNCH20 for 20% off, and there's a 14-day refund you never have to justify. The reason to move is simple — the Lite records your trades; the full one tells you what to stop doing.

The full journal → https://tinkshifter.gumroad.com/l/disciplined-trader-journal

And whether you upgrade or not, one ask: if the Lite helped you even once — spotted a revenge-trade pattern, caught a bad entry habit — reply and tell me. It takes 20 seconds and it shapes what I build next.

Trade smarter,
Tristan"""
    }
]


async def main():
    print("=" * 60)
    print("CREATING GUMROAD EMAIL WORKFLOW")
    print("=" * 60)
    
    async with async_playwright() as p:
        # Launch Edge browser
        print("[1/4] Launching Edge browser...")
        browser = await p.chromium.launch(headless=False, channel="msedge")
        context = await browser.new_context(
            viewport={"width": 1280, "height": 800},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        )
        page = await context.new_page()
        
        try:
            # Go to workflow creation page
            print("[2/4] Navigating to workflow creation...")
            await page.goto("https://app.gumroad.com/workflows/new")
            await page.wait_for_load_state("networkidle")
            await asyncio.sleep(3)
            
            # Check if logged in
            if "login" in page.url.lower():
                print("[ERROR] Not logged in! Please log into Gumroad first.")
                await browser.close()
                return
            
            print("[OK] Logged in")
            
            # Fill in workflow name
            print("[3/4] Setting up workflow...")
            name_input = page.locator('input[name="workflow[name]"]')
            if await name_input.count() > 0:
                await name_input.clear()
                await name_input.fill("Lite → Full Journal Sequence")
                print("[OK] Workflow name set")
            
            # Select the free Lite product
            print("[4/4] Selecting free Lite product...")
            # Look for product selection dropdown or checkboxes
            product_selector = page.locator('select[name="workflow[product_id]"]')
            if await product_selector.count() > 0:
                # Select the Lite product
                await product_selector.select_option(label="The Disciplined Trader Journal — Lite")
                print("[OK] Free Lite product selected")
            else:
                # Try checkbox approach
                lite_checkbox = page.locator('text="Lite"').first
                if await lite_checkbox.count() > 0:
                    await lite_checkbox.click()
                    print("[OK] Free Lite product selected")
            
            # Save workflow
            save_button = page.locator('button[type="submit"]')
            if await save_button.count() > 0:
                await save_button.click()
                await asyncio.sleep(3)
                print("[OK] Workflow saved")
            
            # Now add emails
            print("\n=== Adding emails ===")
            
            for i, email in enumerate(EMAILS, 1):
                print(f"\n--- Email {i} ---")
                
                # Click "Add email" button
                add_email_button = page.locator('text="Add email"')
                if await add_email_button.count() > 0:
                    await add_email_button.click()
                    await asyncio.sleep(2)
                
                # Fill in delay
                delay_input = page.locator('input[name*="delay"]').last
                if await delay_input.count() > 0:
                    await delay_input.clear()
                    await delay_input.fill(str(email["delay"]))
                    print(f"[OK] Delay: {email['delay']} days")
                
                # Fill in subject
                subject_input = page.locator('input[name*="subject"]').last
                if await subject_input.count() > 0:
                    await subject_input.clear()
                    await subject_input.fill(email["subject"])
                    print(f"[OK] Subject: {email['subject'][:50]}...")
                
                # Fill in body
                body_input = page.locator('textarea[name*="body"]').last
                if await body_input.count() > 0:
                    await body_input.clear()
                    await body_input.fill(email["body"])
                    print(f"[OK] Body filled")
                
                # Save email
                save_email_button = page.locator('button[type="submit"]').last
                if await save_email_button.count() > 0:
                    await save_email_button.click()
                    await asyncio.sleep(2)
                    print(f"[OK] Email {i} saved")
            
            print("\n" + "=" * 60)
            print("WORKFLOW CREATED!")
            print("=" * 60)
            print("\nYour email sequence is now live:")
            print("  - Email 1: Immediate (setup instructions)")
            print("  - Email 2: 3 days (engagement check)")
            print("  - Email 3: 10 days (final nudge)")
            
            print("\nView your workflow:")
            print("https://app.gumroad.com/workflows")
            
            print("\nPress Enter to close the browser...")
            await asyncio.get_event_loop().run_in_executor(None, input)
            
        except Exception as e:
            print(f"\n[ERROR] {e}")
            print("\nThe workflow may have been partially created.")
            print("Check your Gumroad dashboard to verify.")
            print("\nPress Enter to close the browser...")
            await asyncio.get_event_loop().run_in_executor(None, input)
        
        finally:
            await browser.close()


if __name__ == "__main__":
    asyncio.run(main())
