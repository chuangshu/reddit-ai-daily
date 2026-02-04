#!/usr/bin/env python3
"""生成日报"""

import json
from datetime import datetime

DATA_FILE = "/root/clawd/reddit-ai/data/reddit_hot.json"
OUTPUT_DIR = "/root/clawd/reddit-ai/daily"

def generate():
    today = datetime.now().strftime("%Y-%m-%d")
    html_file = f"{OUTPUT_DIR}/{today}.html"
    
    # 读取数据
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            posts = json.load(f)
    except:
        posts = []
    
    # 生成 HTML
    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>Reddit AI 情报 - {today}</title>
    <style>
        body {{ font-family: system-ui, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }}
        .post {{ border: 1px solid #ddd; padding: 15px; margin: 10px 0; border-radius: 8px; }}
        .title {{ font-size: 18px; color: #1a1a1b; font-weight: bold; }}
        .meta {{ color: #878a8c; font-size: 12px; margin-top: 5px; }}
        .hot {{ background: #fff3cd; }}
        a {{ color: #0079d3; text-decoration: none; }}
        a:hover {{ text-decoration: underline; }}
    </style>
</head>
<body>
    <h1>⚡ Reddit AI 情报 - {today}</h1>
    <p>🤖 数据来源：r/artificial, r/MachineLearning, r/OpenAI</p>
    <p>📅 更新时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
    <hr>
"""
    
    if posts:
        html += f"<h2>🔥 热门帖子 TOP 10</h2>"
        for i, post in enumerate(posts[:10], 1):
            html += f"""
<div class="post hot">
    <div class="title">{i}. <a href="{post['url']}" target="_blank">{post['title']}</a></div>
    <div class="meta">
        📍 r/{post['subreddit']} | 👍 {post['score']} | 💬 {post['comments']}
    </div>
</div>
"""
    else:
        html += "<p>暂无热门帖子数据</p>"
    
    html += """
    <hr>
    <p>🤖 自动生成 by GitHub Actions</p>
</body>
</html>"""
    
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(html)
    
    print(f"Generated: {html_file}")

if __name__ == "__main__":
    generate()
