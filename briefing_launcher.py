# -*- coding: utf-8 -*-
"""每日技术简报 — 一键启动器"""
import subprocess, sys, os

SCRIPTS = os.path.dirname(os.path.abspath(__file__))

print()
print("  " + "=" * 40)
print("  每日技术简报")
print("  " + "=" * 40)
print()

# Step 1: scrape
print("  [1/2] 抓取 GitHub Trending...")
trending_py = os.path.join...[truncated]