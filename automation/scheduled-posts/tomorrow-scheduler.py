#!/usr/bin/env python3
"""
Scheduled posting for tomorrow with phone notifications
Posts at 8 AM and 12 PM, sends notifications when done
"""

import schedule
import time
import subprocess
import json
from datetime import datetime, timedelta
import requests

# ==================== CONFIGURATION ====================

# Posts to schedule
POSTS = [
    {
        "time": "08:00",
        "text": """Spread costs kill more scalpers than bad entries.

$0.02 spread × 500 shares = $10 per round trip.

10 trades/day = $100/day gone before you're right or wrong about anything.

If you're not tracking it separately, you don't know your real edge.""",
        "image": None,
        "label": "Spread costs post"
    },
    {
        "time": "12:00",
        "text": """R-multiple reminder:

You can be profitable at a 40% win rate with 1.5R average.
You can blow up at a 70% win rate with 0.4R average.

Win rate is a vanity metric. Average R is the number.

Your journal should compute it for you.""",
        "image": None,
        "label": "R-multiples post"
    }
]

# Notification settings (choose one)
NOTIFICATION_METHOD = "pushover"  # Options: "pushover", "email", "telegram", "none"

# Pushover settings (free, sends push notifications to your phone)
PUSHOVER_USER_KEY = "u4s6xys1bvkjbp5du36whquyh1onjk"  # Your User Key
PUSHOVER_APP_TOKEN = "ashtu2j2fkmfwik6svgux6ujrydkoh"  # Your App Token

# Email settings (using email-to-SMS gateway)
EMAIL_TO_SMS = ""  # e.g., "5551234567@txt.att.net" for AT&T

# Telegram settings
TELEGRAM_BOT_TOKEN = ""  # Get from @BotFather
TELEGRAM_CHAT_ID = ""  # Your chat ID

# ==================== NOTIFICATION FUNCTIONS ====================

def send_pushover(title, message):
    """Send push notification via Pushover"""
    if not PUSHOVER_USER_KEY or not PUSHOVER_APP_TOKEN:
        print("[SKIP] Pushover not configured")
        return False
    
    try:
        resp = requests.post("https://api.pushover.net/1/messages.json", data={
            "token": PUSHOVER_APP_TOKEN,
            "user": PUSHOVER_USER_KEY,
            "title": title,
            "message": message
        })
        if resp.status_code == 200:
            print(f"[OK] Pushover notification sent: {title}")
            return True
        else:
            print(f"[ERROR] Pushover failed: {resp.text}")
            return False
    except Exception as e:
        print(f"[ERROR] Pushover error: {e}")
        return False


def send_email_sms(to, subject, body):
    """Send email (works with email-to-SMS gateways)"""
    if not to:
        print("[SKIP] Email not configured")
        return False
    
    try:
        # Using PowerShell to send email
        cmd = f'powershell -Command "Send-MailMessage -To \'{to}\' -From \'scheduler@scalpersedge.com\' -Subject \'{subject}\' -Body \'{body}\' -SmtpServer \'smtp.gmail.com\' -Port 587 -UseSsl"'
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"[OK] Email sent to {to}")
            return True
        else:
            print(f"[ERROR] Email failed: {result.stderr}")
            return False
    except Exception as e:
        print(f"[ERROR] Email error: {e}")
        return False


def send_telegram(message):
    """Send message via Telegram bot"""
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        print("[SKIP] Telegram not configured")
        return False
    
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        resp = requests.post(url, data={
            "chat_id": TELEGRAM_CHAT_ID,
            "text": message,
            "parse_mode": "HTML"
        })
        if resp.status_code == 200:
            print(f"[OK] Telegram message sent")
            return True
        else:
            print(f"[ERROR] Telegram failed: {resp.text}")
            return False
    except Exception as e:
        print(f"[ERROR] Telegram error: {e}")
        return False


def notify(title, message):
    """Send notification using configured method"""
    print(f"\n{'='*50}")
    print(f"NOTIFICATION: {title}")
    print(f"{'='*50}")
    print(f"{message}\n")
    
    if NOTIFICATION_METHOD == "pushover":
        send_pushover(title, message)
    elif NOTIFICATION_METHOD == "email":
        send_email_sms(EMAIL_TO_SMS, title, message)
    elif NOTIFICATION_METHOD == "telegram":
        send_telegram(f"<b>{title}</b>\n\n{message}")
    else:
        print("[INFO] Notifications disabled")


# ==================== POSTING FUNCTIONS ====================

def post_tweet(post):
    """Post a tweet using OpenCLI"""
    print(f"\n{'='*50}")
    print(f"POSTING: {post['label']}")
    print(f"{'='*50}")
    
    try:
        # Build command
        cmd = f'opencli twitter post "{post["text"]}" --window background -f yaml'
        
        # Add image if provided
        if post.get("image"):
            cmd = f'opencli twitter post "{post["text"]}" --images "{post["image"]}" --window background -f yaml'
        
        # Execute
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=60)
        
        if result.returncode == 0 and "success" in result.stdout.lower():
            print(f"[OK] Tweet posted successfully!")
            
            # Extract URL from response
            for line in result.stdout.split('\n'):
                if 'url:' in line:
                    url = line.split('url:')[1].strip()
                    print(f"URL: {url}")
                    
                    # Send notification
                    notify(
                        "Tweet Posted!",
                        f"{post['label']} posted successfully!\n\nURL: {url}\n\nTime: {datetime.now().strftime('%I:%M %p')}"
                    )
                    return True
        else:
            print(f"[ERROR] Post failed: {result.stdout} {result.stderr}")
            notify("Post Failed!", f"{post['label']} failed to post.\n\nError: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"[ERROR] {e}")
        notify("Post Error!", f"{post['label']} encountered an error:\n{e}")
        return False


def check_and_post(post_time, post):
    """Check if it's time to post"""
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    
    if current_time == post_time:
        post_tweet(post)


# ==================== MAIN SCHEDULER ====================

def main():
    print("=" * 60)
    print("TOMORROW'S POSTING SCHEDULER")
    print("=" * 60)
    
    # Calculate tomorrow's date
    tomorrow = datetime.now() + timedelta(days=1)
    print(f"\nScheduled for: {tomorrow.strftime('%A, %B %d, %Y')}")
    print(f"Current time: {datetime.now().strftime('%I:%M %p')}")
    
    # Display schedule
    print("\nScheduled posts:")
    for post in POSTS:
        print(f"  {post['time']} - {post['label']}")
    
    # Display notification method
    print(f"\nNotification method: {NOTIFICATION_METHOD}")
    if NOTIFICATION_METHOD == "none":
        print("(Notifications disabled)")
    
    print("\n" + "=" * 60)
    print("Starting scheduler... (Press Ctrl+C to stop)")
    print("=" * 60)
    
    # Schedule posts
    for post in POSTS:
        schedule.every().day.at(post["time"]).do(check_and_post, post["time"], post)
        print(f"Scheduled: {post['label']} at {post['time']}")
    
    # Send startup notification
    notify(
        "Scheduler Started!",
        f"Tomorrow's posts are scheduled!\n\n"
        f"Post 1: 8:00 AM - Spread costs\n"
        f"Post 2: 12:00 PM - R-multiples\n\n"
        f"Your manual post reminder will come at 3:00 PM"
    )
    
    # Run scheduler
    try:
        while True:
            schedule.run_pending()
            time.sleep(30)  # Check every 30 seconds
    except KeyboardInterrupt:
        print("\n\nScheduler stopped by user")
        notify("Scheduler Stopped", "The posting scheduler has been stopped.")


if __name__ == "__main__":
    main()
