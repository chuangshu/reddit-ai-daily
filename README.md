# Reddit AI 情报日报

## 部署方法

1. Fork 本仓库
2. 开启 GitHub Pages（Settings → Pages → main branch）
3. 配置定时任务抓取数据

## 定时任务

```bash
0 9 * * * cd /root/clawd/reddit-ai && ./scripts/fetch_all.sh >> logs/fetch.log 2>&1
```

## 贡献者

基于 nutllwhy/reddit-AI 改造
