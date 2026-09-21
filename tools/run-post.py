#!/usr/bin/env python3
"""
Simple script to run a scheduled post
Usage: python run-post.py [8am|12pm]
"""

import subprocess
import requests
import sys

# Pushover credentials
PUSHOVER_TOKEN = "ashtu2j2fkmfwik6svgux6ujrydkoh"
PUSHOVER_USER = "u4s6xys1bvkjbp5du36whquyh1onjk"

# Posts
POSTS = {
    "8am": {
        "text": """Spread costs kill more scalpers than bad entries.

$0.02 spread × 500 shares = $10 per round trip.

10 trades/day = $100/day gone before you're right or wrong about anything.

If you're not tracking it separately, you don't know your real edge.""",
        "label": "Spread costs post"
    },
    "12pm": {
        "text": """R-multiple reminder:

You can be profitable at a 40% win rate with 1.5R average.
You can blow up at a 70% win rate with 0.4R average.

Win rate is a vanity metric. Average R is the number.

Your journal should compute it for you.""",
        "label": "R-multiples post"
    }
}

def notify(title, message):
    """Send push notification"""
    try:
        requests.post('https://api.pushover.net/1/messages.json', data={
            'token': PUSHOVER_TOKEN,
            'user': PUSHOVER_USER,
            'title': title,
            'message': message
        })
    except:
        pass

def main():
    if len(sys.argv) < 2:
        print("Usage: python run-post.py [8am|12pm]")
        sys.exit(1)
    
    post_time = sys.argv[1].lower()
    if post_time not in POSTS:
        print(f"Invalid time: {post_time}. Use '8am' or '12pm'")
        sys.exit(1)
    
    post = POSTS[post_time]
    print(f"Posting: {post['label']}")
    
    try:
        cmd = f'opencli twitter post "{post["text"]}" --window background -f yaml'
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=60)
        
        if 'success' in result.stdout.lower():
            print("[OK] Post successful!")
            for line in result.stdout.split('\n'):
                if 'url:' in line:
                    url = line.split('url:')[1].strip()
                    print(f"URL: {url}")
            notify("Tweet Posted!", f"{post['label']} is now live!")
        else:
            print("[ERROR] Post failed!")
            print(result.stderr)
            notify("Post Failed!", f"{post['label']} failed to post.")
    except Exception as e:
        print(f"Error: {e}")
        notify("Post Error!", str(e))

if __name__ == "__main__":
    main()
