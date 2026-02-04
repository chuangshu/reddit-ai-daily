#!/bin/bash
# 生成 Reddit AI 情报日报

DATE=$(date +%Y-%m-%d)
OUTPUT_DIR="/root/clawd/reddit-ai/daily"
TEMPLATE_DIR="/root/clawd/reddit-ai/templates"

# 创建 HTML
cat > "${OUTPUT_DIR}/${DATE}.html" << HTML
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>Reddit AI 情报 - ${DATE}</title>
    <style>
        body { font-family: system-ui, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }
        .post { border: 1px solid #ddd; padding: 15px; margin: 10px 0; border-radius: 8px; }
        .title { font-size: 18px; color: #1a1a1b; }
        .meta { color: #878a8c; font-size: 12px; margin-top: 5px; }
        .highlight { background: #f8f9fa; }
    </style>
</head>
<body>
    <h1>⚡ Reddit AI 情报 - ${DATE}</h1>
    <p>数据来源：r/artificial, r/MachineLearning, r/OpenAI</p>
    <hr>
    <!-- 帖子内容将由 fetch 脚本填充 -->
    <p>今日暂无热门帖子数据</p>
</body>
</html>
HTML

echo "Generated: ${OUTPUT_DIR}/${DATE}.html"
