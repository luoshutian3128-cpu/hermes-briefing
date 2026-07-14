#!/usr/bin/env python3
"""开源项目 Trending 爬虫 — GitHub 优先，Gitee 降级。
用法: python trending.py [daily|weekly]
"""
import json, re, sys, time, urllib.request
from datetime import datetime

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

URL = "htt...[truncated]