#!/usr/bin/env python3
"""
小红书爆款文案生成器 API服务器
部署到公网后，用户调用时会先扣费，再返回文案

SkillPay配置:
- Skill ID: 0867e1ac-78e6-4d26-8e45-a365459c4108
- API Key: sk_939c573633ec6255d5faf911de763e9a2d127e51384a1ae403b271c746206a47
"""

from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# SkillPay配置
SKILL_ID = "0867e1ac-78e6-4d26-8e45-a365459c4108"
API_KEY = "sk_939c573633ec6255d5faf911de763e9a2d127e51384a1ae403b271c746206a47"
BILLING_API_URL = "https://skillpay.me/api/v1/billing"


def charge_user(user_id: str) -> dict:
    """扣费 - 每次调用扣费0.01 USDT"""
    try:
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
            },
            timeout=10
        )
        data = resp.json()
        if data.get("success"):
            return {"ok": True, "balance": data.get("balance")}
        return {
            "ok": False,
            "balance": data.get("balance", 0),
            "payment_url": data.get("payment_url")
        }
    except Exception as e:
        return {"ok": False, "error": str(e)}


def generate_viral_copy(topic: str) -> dict:
    """生成小红书爆款文案"""
    
    if "http" in topic:
        content_type = "复刻爆款"
        hook = "姐妹们！这个真的太绝了！"
    else:
        content_type = "原创爆款"
        hook = f"姐妹们！{topic}也太香了吧！"
    
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


@app.route('/')
def index():
    """主页 - 使用说明"""
    return """
    <html>
    <head>
        <title>小红书爆款文案生成器</title>
    </head>
    <body>
        <h1>小红书爆款文案生成器 API</h1>
        <p>使用方式：</p>
        <pre>
POST /api
{
    "user_id": "用户ID",
    "topic": "主题"
}
        </pre>
        <p>价格：0.01 USDT/次</p>
    </body>
    </html>
    """

@app.route('/api', methods=['POST'])
def handle_request():
    """API入口 - SkillPay会调用这个接口"""
    data = request.get_json()
    
    # SkillPay会传递user_id
    user_id = data.get('user_id', 'anonymous')
    # 用户请求的内容
    topic = data.get('topic', data.get('message', '好物分享'))
    
    # 1. 先扣费
    charge_result = charge_user(user_id)
    
    if not charge_result["ok"]:
        # 余额不足，返回充值链接
        return jsonify({
            "success": False,
            "message": "余额不足，请先充值",
            "payment_url": charge_result.get("payment_url"),
            "balance": charge_result.get("balance", 0)
        })
    
    # 2. 扣费成功，生成文案
    result = generate_viral_copy(topic)
    result["success"] = True
    result["message"] = "生成成功！"
    result["balance"] = charge_result["balance"]
    
    return jsonify(result)


@app.route('/health', methods=['GET'])
def health():
    """健康检查"""
    return jsonify({"status": "ok"})


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print("=== Xiaohongshu Viral Copy API Server ===")
    print(f"Port: {port}")
    print(f"Skill ID: {SKILL_ID}")
    app.run(host='0.0.0.0', port=port)
