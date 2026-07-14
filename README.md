# Hermes Daily Briefing

基于 Hermes Agent 的每日技术简报工具。自动抓取 GitHub Trending，筛选 AI/Agent 相关项目，生成中文简报。

## 特性

- 🔄 **双源降级**：GitHub Trending（全局）→ Gitee（国内）自动切换
- 🤖 **AI 摘要**：自动筛选 AI/Agent/LLM 相关项目
- 📊 **结构化输出**：每日生成 Markdown 简报
- 🖱️ **一行命令**：`python trending.py` 即可

## 快速开始

```bash
# 抓取 Trending
python trending.py

# 在 Hermes 中对我说：
# "读取 trending_today.json，生成今日简报"
```

## 文件说明

| 文件 | 用途 |
|------|------|
| `trending.py` | 双源爬虫，GitHub + Gitee 自动降级 |
| `briefing_launcher.py` | 一键启动器 |

## 依赖

- Python 3.10+
- 纯标准库，无需 pip install
- GitHub 访问需 VPN（国内）

## 示例

📊 GitHub Trending 简报 — 2026年7月14日

▸ DesktopCommanderMCP ⭐+909
  Claude 终端控制 MCP 服务器

▸ superpowers ⭐+740
  Agent Skills 框架

💡 MCP 标准化 + Agent Skills 生态持续爆发

## License

MIT
