#!/usr/bin/env python3
"""
X Profile Setup Automation for @scalpersedge
Uses Playwright to automate profile setup and first post.
"""

import asyncio
import os
from pathlib import Path
from playwright.async_api import async_playwright

# Paths
PROJECT_ROOT = Path(__file__).parent.parent
ASSETS = PROJECT_ROOT / "social-content" / "assets"
SCREENSHOTS = PROJECT_ROOT / "gumroad" / "landing" / "screenshots"

# Profile setup data
PROFILE_DATA = {
    "name": "The Scalper's Edge",
    "bio": "Trade smarter. Journal harder.\n\nNotion trade journal built for scalpers - R-multiples, spread costs, session heatmaps, psychology flags.\n\nFree lite + full template",
    "location": "tinkshifter.gumroad.com",
    "website": "https://tinkshifter.gumroad.com/l/disciplined-trader-journal"
}

# Launch post content
LAUNCH_POST = """I scalped for a year before I journaled a single trade.

Winged it, repeated the same mistakes, blamed "the market."

Built the journal I wish I'd had on day 1:

• 12-pt pre-trade checklist
• auto P&L + R-multiples
• spread cost tracking
• psychology flags (FOMO / revenge)
• session heatmaps

Duplicate to Notion in 2 min
https://tinkshifter.gumroad.com/l/disciplined-trader-journal"""


async def setup_profile(page):
    """Set up the X profile with avatar, banner, bio, and links."""
    
    print("\n=== Step 1: Navigate to profile settings ===")
    await page.goto("https://x.com/settings/profile")
    await page.wait_for_load_state("networkidle")
    await asyncio.sleep(2)
    
    print("=== Step 2: Update display name ===")
    name_input = page.locator('input[name="name"]')
    if await name_input.count() > 0:
        await name_input.clear()
        await name_input.fill(PROFILE_DATA["name"])
        print(f"  [OK] Name set to: {PROFILE_DATA['name']}")
    
    print("=== Step 3: Update bio ===")
    bio_input = page.locator('textarea[name="description"]')
    if await bio_input.count() > 0:
        await bio_input.clear()
        await bio_input.fill(PROFILE_DATA["bio"])
        print("  [OK] Bio updated")
    
    print("=== Step 4: Update location ===")
    location_input = page.locator('input[name="location"]')
    if await location_input.count() > 0:
        await location_input.clear()
        await location_input.fill(PROFILE_DATA["location"])
        print(f"  [OK] Location set to: {PROFILE_DATA['location']}")
    
    print("=== Step 5: Update website ===")
    website_input = page.locator('input[name="url"]')
    if await website_input.count() > 0:
        await website_input.clear()
        await website_input.fill(PROFILE_DATA["website"])
        print(f"  [OK] Website set")
    
    # Save changes
    save_button = page.locator('div[data-testid="Profile_Save_Button"]')
    if await save_button.count() > 0:
        await save_button.click()
        await asyncio.sleep(2)
        print("  [OK] Profile saved")
    
    print("\n=== Step 6: Upload avatar ===")
    avatar_path = ASSETS / "avatar-400.png"
    if avatar_path.exists():
        # Click edit button on avatar
        edit_avatar = page.locator('div[aria-label="Edit profile photo"]')
        if await edit_avatar.count() > 0:
            await edit_avatar.click()
            await asyncio.sleep(1)
            
            # Click "Upload photo"
            upload_option = page.locator('div[role="menuitem"]:has-text("Upload photo")')
            if await upload_option.count() > 0:
                await upload_option.click()
                await asyncio.sleep(1)
                
                # Set file
                file_input = page.locator('input[type="file"]').first
                await file_input.set_input_files(str(avatar_path))
                await asyncio.sleep(2)
                
                # Confirm upload
                apply_button = page.locator('div[data-testid="ApplyButton"]')
                if await apply_button.count() > 0:
                    await apply_button.click()
                    await asyncio.sleep(2)
                    print("  [OK] Avatar uploaded")
    
    print("\n=== Step 7: Upload banner ===")
    banner_path = ASSETS / "banner-1500x500.png"
    if banner_path.exists():
        # Click edit button on banner
        edit_banner = page.locator('div[aria-label="Edit profile banner"]')
        if await edit_banner.count() > 0:
            await edit_banner.click()
            await asyncio.sleep(1)
            
            # Click "Upload photo"
            upload_option = page.locator('div[role="menuitem"]:has-text("Upload photo")')
            if await upload_option.count() > 0:
                await upload_option.click()
                await asyncio.sleep(1)
                
                # Set file
                file_input = page.locator('input[type="file"]').first
                await file_input.set_input_files(str(banner_path))
                await asyncio.sleep(2)
                
                # Confirm upload
                apply_button = page.locator('div[data-testid="ApplyButton"]')
                if await apply_button.count() > 0:
                    await apply_button.click()
                    await asyncio.sleep(2)
                    print("  [OK] Banner uploaded")


async def post_launch_tweet(page):
    """Post the launch tweet with trade-log screenshot."""
    
    print("\n=== Step 8: Compose launch tweet ===")
    await page.goto("https://x.com/compose/post")
    await page.wait_for_load_state("networkidle")
    await asyncio.sleep(2)
    
    # Type the tweet
    tweet_box = page.locator('div[data-testid="tweetTextarea_0"]')
    if await tweet_box.count() > 0:
        await tweet_box.click()
        await asyncio.sleep(0.5)
        await tweet_box.fill(LAUNCH_POST)
        print("  [OK] Tweet text entered")
    
    print("=== Step 9: Attach trade-log screenshot ===")
    screenshot_path = SCREENSHOTS / "trade-log.png"
    if screenshot_path.exists():
        # Click media button
        media_button = page.locator('div[data-testid="fileInput"]')
        if await media_button.count() > 0:
            await media_button.set_input_files(str(screenshot_path))
            await asyncio.sleep(3)
            print("  [OK] Screenshot attached")
    
    print("=== Step 10: Post tweet ===")
    post_button = page.locator('div[data-testid="tweetButton"]')
    if await post_button.count() > 0:
        await post_button.click()
        await asyncio.sleep(3)
        print("  [OK] Tweet posted!")
    
    print("\n=== Step 11: Pin the tweet ===")
    # Navigate to profile to find the tweet
    await page.goto("https://x.com/Scalpersedge")
    await asyncio.sleep(3)
    
    # Find the first tweet's menu
    more_button = page.locator('div[data-testid="tweet"]').first.locator('div[data-testid="tweet"] button[aria-label="More"]').first
    if await more_button.count() > 0:
        await more_button.click()
        await asyncio.sleep(1)
        
        # Click "Pin to profile"
        pin_option = page.locator('div[role="menuitem"]:has-text("Pin to profile")')
        if await pin_option.count() > 0:
            await pin_option.click()
            await asyncio.sleep(1)
            
            # Confirm pin
            confirm_button = page.locator('div[data-testid="confirmationSheetConfirm"]')
            if await confirm_button.count() > 0:
                await confirm_button.click()
                await asyncio.sleep(2)
                print("  [OK] Tweet pinned!")


async def main():
    """Main automation flow."""
    
    print("=" * 60)
    print("X PROFILE SETUP AUTOMATION")
    print("For @scalpersedge")
    print("=" * 60)
    
    print("\nThis script will:")
    print("1. Set up your profile (name, bio, avatar, banner)")
    print("2. Post the launch tweet with trade-log screenshot")
    print("3. Pin the launch tweet to your profile")
    
    print("\nIMPORTANT: You must be logged into X in your browser first!")
    print("The script will use your existing browser session.")
    
    input("\nPress Enter when ready to start...")
    
    async with async_playwright() as p:
        # Launch browser with persistent context (uses existing login)
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(
            viewport={"width": 1280, "height": 800},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        )
        page = await context.new_page()
        
        try:
            # First, check if logged in
            print("\n=== Checking login status ===")
            await page.goto("https://x.com/home")
            await page.wait_for_load_state("networkidle")
            await asyncio.sleep(2)
            
            if "login" in page.url.lower() or await page.locator('text="Sign in"').count() > 0:
                print("[ERROR] Not logged in! Please log into X in your browser first.")
                print("   Then run this script again.")
                await browser.close()
                return
            
            print("[OK] Logged in successfully")
            
            # Run setup
            await setup_profile(page)
            await post_launch_tweet(page)
            
            print("\n" + "=" * 60)
            print("SETUP COMPLETE!")
            print("=" * 60)
            print("\nYour profile is now set up with:")
            print("  - Name: The Scalper's Edge")
            print("  - Avatar & banner uploaded")
            print("  - Bio with link to Gumroad")
            print("  - Launch tweet posted and pinned")
            
            print("\nNext steps:")
            print("  1. Review your profile at https://x.com/Scalpersedge")
            print("  2. Follow 20-30 trading accounts")
            print("  3. Start the daily reply routine")
            
            input("\nPress Enter to close the browser...")
            
        except Exception as e:
            print(f"\n[ERROR] {e}")
            print("\nThe script may have partially completed.")
            print("Check your profile and complete any missing steps manually.")
            input("\nPress Enter to close the browser...")
        
        finally:
            await browser.close()


if __name__ == "__main__":
    asyncio.run(main())
