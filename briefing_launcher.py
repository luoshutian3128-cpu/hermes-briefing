# -*- coding: utf-8 -*-
"""每日技术简报 — 一键生成"""
import subprocess, sys, os, json

print()
print("  " + "=" * 40)
print("  每日技术简报")
print("  " + "=" * 40)
print()

print("  [1/2] 抓取 GitHub Trending...")
result = subprocess.run(
    [sys.executable, "E:/Hermes/home/scripts/trending.py"],
    capture_output=True, text=True, encoding="utf-8", errors="replace",
)

if result.returncode != 0:
    print()
    print("  ❌ 抓取失败: GitHub 不可达")
    print()
    print("  可能原因和解决办法:")
    print("    1. VPN 未开启 → 打开 VPN 后重试")
    print("    2. VPN 节点慢 → 换个节点")
    print("    3. 想用国内源 → 执行: python trending.py weekly")
    print("       (Gitee 直连，无需 VPN)")
    print()
    input("按回车退出...")
    sys.exit(1)

out_path = "E:/Hermes/home/trending_today.json"
with open(out_path, "w", encoding="utf-8") as f:
    f.write(result.stdout)

data = json.loads(result.stdout)
print(f"  ✅ 获取 {data['count']} 个项目 (源: {data['source']})")

print()
print("  [2/2] 在 Hermes 里对我说：")
print()
print("        读取 trending_today.json，生成今日简报")
print()
print("  " + "=" * 40)
input("按回车退出...")
