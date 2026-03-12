#!/usr/bin/env python3
"""
小红书爆款文案生成器 Skill
Skill ID: 0867e1ac-78e6-4d26-8e45-a365459c4108
价格: 0.01 USDT/次

用法:
    python xiaohongshu_viral_copy.py <user_id> "<主题或爆款笔记URL>"
"""

import requests
import json
import sys
import os

# SkillPay 配置
SKILL_ID = "0867e1ac-78e6-4d26-8e45-a365459c4108"
API_KEY = "sk_939c573633ec6255d5faf911de763e9a2d127e51384a1ae403b271c746206a47"
BILLING_API_URL = "https://skillpay.me/api/v1/billing"


def charge_user(user_id: str) -> dict:
    """扣费 - 每次调用扣费"""
    resp = requests.post(
        f"{BILLING_API_URL}/charge",
        headers={
            "X-API-Key": API_KEY,
            "Content-Type": "application/json"
        },
        json={
            "user_id": user_id,
            "skill_id": SKILL_ID,
            "amount": 0.01
        }
    )
    data = resp.json()
    if data.get("success"):
        return {"ok": True, "balance": data.get("balance")}
    return {
        "ok": False,
        "balance": data.get("balance", 0),
        "payment_url": data.get("payment_url")
    }


def check_balance(user_id: str) -> float:
    """查余额"""
    resp = requests.get(
        f"{BILLING_API_URL}/balance?user_id={user_id}",
        headers={"X-API-Key": API_KEY}
    )
    data = resp.json()
    return data.get("balance", 0)


def generate_viral_copy(topic: str) -> dict:
    """生成小红书爆款文案"""
    
    # 分析话题或直接生成文案
    if "http" in topic:
        # 如果是URL，复刻该爆款的结构
        content_type = "复刻爆款"
        hook = "姐妹们！这个真的太绝了！"
    else:
        # 如果是主题，生成新的爆款文案
        content_type = "原创爆款"
        hook = f"姐妹们！{topic}也太香了吧！"
    
    # 生成文案结构
    result = {
        "hook": hook,
        "body": [
            f"姐妹们！今天必须跟你们聊聊{topic}！",
            "说实话一开始我也没当回事，直到...",
            "用了一段时间后真的惊到了！",
            "特别是最后一点，简直了！"
        ],
        "cta": "你们觉得怎么样？评论区聊聊～",
        "hashtags": [f"#{topic}", "#种草", "#真实分享", "#必看", "#好物推荐"]
    }
    
    return result


def main():
    if len(sys.argv) < 3:
        print(json.dumps({
            "error": "用法: python skill.py <user_id> <主题或URL>"
        }))
        sys.exit(1)
    
    user_id = sys.argv[1]
    topic = sys.argv[2]
    
    # 1. 先扣费
    charge_result = charge_user(user_id)
    
    if not charge_result["ok"]:
        # 余额不足，返回充值链接
        print(json.dumps({
            "success": False,
            "message": "余额不足，请先充值",
            "payment_url": charge_result["payment_url"],
            "balance": charge_result["balance"]
        }, ensure_ascii=False))
        sys.exit(1)
    
    # 2. 扣费成功，生成文案
    result = generate_viral_copy(topic)
    result["success"] = True
    result["message"] = "生成成功！"
    result["balance"] = charge_result["balance"]
    
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
