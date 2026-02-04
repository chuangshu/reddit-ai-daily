#!/usr/bin/env python3
"""Reddit AI 热门帖子抓取"""

import urllib.request
import json
from datetime import datetime

SUBREDDITS = ["artificial", "MachineLearning", "OpenAI"]
OUTPUT_FILE = "/root/clawd/reddit-ai/data/reddit_hot.json"

def fetch_reddit():
    posts = []
    
    for sub in SUBREDDITS:
        url = f"https://www.reddit.com/r/{sub}/hot.json?limit=10"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }
        
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=10) as response:
                data = json.loads(response.read().decode())
                for post in data.get("data", {}).get("children", []):
                    post_data = post.get("data", {})
                    if post_data.get("score", 0) > 100:  # 热度门槛
                        posts.append({
                            "subreddit": sub,
                            "title": post_data.get("title", ""),
                            "score": post_data.get("score", 0),
                            "url": f"https://reddit.com{post_data.get('permalink', '')}",
                            "comments": post_data.get("num_comments", 0),
                            "created": datetime.fromtimestamp(post_data.get("created_utc", 0)).isoformat()
                        })
        except Exception as e:
            print(f"Error fetching r/{sub}: {e}")
    
    # 按热度排序
    posts.sort(key=lambda x: x["score"], reverse=True)
    
    # 保存
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(posts, f, ensure_ascii=False, indent=2)
    
    print(f"Saved {len(posts)} posts to {OUTPUT_FILE}")

if __name__ == "__main__":
    fetch_reddit()
