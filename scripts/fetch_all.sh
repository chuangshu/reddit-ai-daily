#!/bin/bash
# Reddit AI 情报日报 - 自动抓取和推送

DATE=$(date +%Y-%m-%d)
REPO_DIR="/root/clawd/reddit-ai"
LOG_DIR="/root/clawd/reddit-ai/logs"

echo "======== $(date) ========" >> $LOG_DIR/fetch.log

cd $REPO_DIR

# 1. 抓取 Reddit 数据
echo "[1] 抓取 Reddit 数据..." >> $LOG_DIR/fetch.log
./scripts/fetch_reddit.sh >> $LOG_DIR/fetch.log 2>&1

# 2. 生成日报
echo "[2] 生成日报..." >> $LOG_DIR/fetch.log
./scripts/generate_daily.sh >> $LOG_DIR/fetch.log 2>&1

# 3. 提交并推送
echo "[3] 推送到 GitHub..." >> $LOG_DIR/fetch.log
git add daily/ data/
git commit -m "📰 更新日报 $DATE" >> $LOG_DIR/fetch.log 2>&1
git push origin main >> $LOG_DIR/fetch.log 2>&1

echo "[✓] 完成" >> $LOG_DIR/fetch.log
