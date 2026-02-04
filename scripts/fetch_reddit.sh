#!/bin/bash
# 获取 Reddit 热门帖子

SUBREDDIT=$1
MIN_UPVOTES=${2:-500}
OUTPUT_DIR=${3:-/root/clawd/reddit-ai/data}

# Reddit RSS feed
RSS_URL="https://www.reddit.com/r/${SUBREDDIT}/top/.rss?t=day"

echo "Fetching r/${SUBREDDIT}..."

# 抓取并解析 RSS
curl -s "$RSS_URL" | grep -oP '<title>[^<]+</title>' | head -20

echo "Done for r/${SUBREDDIT}"
