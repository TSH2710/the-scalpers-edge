#!/usr/bin/env python3
"""
X Profile Setup - Fresh browser for profile setup and tweet pinning
"""

import asyncio
from pathlib import Path
from playwright.async_api import async_playwright

# Paths
PROJECT_ROOT = Path(__file__).parent.parent
ASSETS = PROJECT_ROOT / "social-content" / "assets"

# Profile setup data
PROFILE_DATA = {
    "name": "The Scalper's Edge",
    "bio": "Trade smarter. Journal harder.\n\nNotion trade journal built for scalpers - R-multiples, spread costs, session heatmaps, psychology flags.\n\nFree lite + full template",
    "location": "tinkshifter.gumroad.com",
    "website": "https://tinkshifter.gumroad.com/l/disciplined-trader-journal"
}

# Tweet URL to pin
TWEET_URL = "https://x.com/Scalpersedge/status/2101764830797439204"


async def main():
    print("=" * 60)
    print("X PROFILE SETUP & PIN TWEET")
    print("=" * 60)
    
    async with async_playwright() as p:
        # Launch fresh Edge browser
        print("[1/6] Launching Edge browser...")
        browser = await p.chromium.launch(headless=False, channel="msedge")
        context = await browser.new_context(
            viewport={"width": 1280, "height": 800},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        )
        page = await context.new_page()
        
        try:
            # Go to X and let user log in
            print("[2/6] Going to X.com - Please log in manually...")
            await page.goto("https://x.com/login")
            await page.wait_for_load_state("networkidle")
            
            # Wait for user to log in
            print("Waiting for you to log in...")
            for i in range(90):  # Wait up to 90 seconds
                await asyncio.sleep(1)
                if "home" in page.url.lower() or await page.locator('[data-testid="primaryColumn"]').count() > 0:
                    print("[OK] Logged in!")
                    break
            else:
                print("[ERROR] Login timeout - please try again")
                await browser.close()
                return
            
            # Setup profile
            print("[3/6] Navigating to profile settings...")
            await page.goto("https://x.com/settings/profile")
            await page.wait_for_load_state("networkidle")
            await asyncio.sleep(2)
            
            print("[4/6] Updating profile fields...")
            # Name
            name_input = page.locator('input[name="name"]')
            if await name_input.count() > 0:
                await name_input.clear()
                await name_input.fill(PROFILE_DATA["name"])
            
            # Bio
            bio_input = page.locator('textarea[name="description"]')
            if await bio_input.count() > 0:
                await bio_input.clear()
                await bio_input.fill(PROFILE_DATA["bio"])
            
            # Location
            location_input = page.locator('input[name="location"]')
            if await location_input.count() > 0:
                await location_input.clear()
                await location_input.fill(PROFILE_DATA["location"])
            
            # Website
            website_input = page.locator('input[name="url"]')
            if await website_input.count() > 0:
                await website_input.clear()
                await website_input.fill(PROFILE_DATA["website"])
            
            # Save
            save_button = page.locator('div[data-testid="Profile_Save_Button"]')
            if await save_button.count() > 0:
                await save_button.click()
                await asyncio.sleep(2)
            
            print("[OK] Profile fields updated")
            
            # Upload avatar
            print("[5/6] Uploading avatar...")
            avatar_path = ASSETS / "avatar-400.png"
            if avatar_path.exists():
                edit_avatar = page.locator('div[aria-label="Edit profile photo"]')
                if await edit_avatar.count() > 0:
                    await edit_avatar.click()
                    await asyncio.sleep(1)
                    
                    upload_option = page.locator('div[role="menuitem"]:has-text("Upload photo")')
                    if await upload_option.count() > 0:
                        await upload_option.click()
                        await asyncio.sleep(1)
                        
                        file_input = page.locator('input[type="file"]').first
                        await file_input.set_input_files(str(avatar_path))
                        await asyncio.sleep(2)
                        
                        apply_button = page.locator('div[data-testid="ApplyButton"]')
                        if await apply_button.count() > 0:
                            await apply_button.click()
                            await asyncio.sleep(2)
            
            print("[OK] Avatar uploaded")
            
            # Upload banner
            print("[6/6] Uploading banner...")
            banner_path = ASSETS / "banner-1500x500.png"
            if banner_path.exists():
                edit_banner = page.locator('div[aria-label="Edit profile banner"]')
                if await edit_banner.count() > 0:
                    await edit_banner.click()
                    await asyncio.sleep(1)
                    
                    upload_option = page.locator('div[role="menuitem"]:has-text("Upload photo")')
                    if await upload_option.count() > 0:
                        await upload_option.click()
                        await asyncio.sleep(1)
                        
                        file_input = page.locator('input[type="file"]').first
                        await file_input.set_input_files(str(banner_path))
                        await asyncio.sleep(2)
                        
                        apply_button = page.locator('div[data-testid="ApplyButton"]')
                        if await apply_button.count() > 0:
                            await apply_button.click()
                            await asyncio.sleep(2)
            
            print("[OK] Banner uploaded")
            
            # Pin the tweet
            print("[BONUS] Pinning launch tweet...")
            await page.goto(TWEET_URL)
            await asyncio.sleep(3)
            
            # Click more button on the tweet
            more_button = page.locator('div[data-testid="tweet"]').first.locator('button[aria-label="More"]').first
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
            
            print("[OK] Tweet pinned!")
            
            print("\n" + "=" * 60)
            print("SETUP COMPLETE!")
            print("=" * 60)
            print("\nYour profile is ready:")
            print("  - Name: The Scalper's Edge")
            print("  - Avatar & banner uploaded")
            print("  - Bio with link to Gumroad")
            print("  - Launch tweet posted and pinned")
            
            print("\nView your profile: https://x.com/Scalpersedge")
            print("\nPress Enter to close the browser...")
            await asyncio.get_event_loop().run_in_executor(None, input)
            
        except Exception as e:
            print(f"\n[ERROR] {e}")
            print("\nThe script may have partially completed.")
            print("Check your profile and complete any missing steps manually.")
            print("\nPress Enter to close the browser...")
            await asyncio.get_event_loop().run_in_executor(None, input)
        
        finally:
            await browser.close()


if __name__ == "__main__":
    asyncio.run(main())
