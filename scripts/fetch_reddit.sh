#!/bin/bash
# 获取 Reddit AI 热门帖子 - 使用搜索方式

OUTPUT_DIR=${1:-/root/clawd/reddit-ai/data}

echo "Fetching Reddit AI热门..."

# 使用 DuckDuckGo 搜索 Reddit AI 热门
QUERY="site:reddit.com/r/artificial OR site:reddit.com/r/MachineLearning OR site:reddit.com/r/OpenAI"

# 搜索并保存结果
curl -s "https://html.duckduckgo.com/html/?q=${QUERY}&t=h&ia=web" > "${OUTPUT_DIR}/reddit_search.html"

echo "Saved: ${OUTPUT_DIR}/reddit_search.html"
echo "Done!"
