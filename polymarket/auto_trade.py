import sys
import os
import json
import time
from datetime import datetime, timezone

# Add workspace to path
sys.path.insert(0, 'C:/Users/Administrator/.openclaw/workspace')
os.chdir('C:/Users/Administrator/.openclaw/workspace/polymarket')

from polymarket.skills import (
    skill_check_portfolio, skill_radar, skill_multi_news_search,
    skill_auto_buy, skill_sell, load_ledger
)

LEDGER_FILE = "ledger.json"

def get_coldown_tokens():
    """Load cooldown tokens from state file"""
    state_file = "state.json"
    if os.path.exists(state_file):
        with open(state_file, 'r') as f:
            state = json.load(f)
        return set(state.get('cooldown_tokens', []))
    return set()

def add_to_cooldown(token_id):
    """Add token to 24h cooldown"""
    state_file = "state.json"
    state = {}
    if os.path.exists(state_file):
        with open(state_file, 'r') as f:
            state = json.load(f)
    
    now = time.time()
    cooldown_tokens = state.get('cooldown_tokens', {})
    # Remove tokens that have passed 24h
    cutoff = now - 24 * 3600
    cooldown_tokens = {k: v for k, v in cooldown_tokens.items() if v > cutoff}
    cooldown_tokens[token_id] = now
    
    state['cooldown_tokens'] = cooldown_tokens
    with open(state_file, 'w') as f:
        json.dump(state, f, indent=2)

def save_state(state):
    with open("state.json", 'w') as f:
        json.dump(state, f, indent=2)

print(f"=== Polymarket 全自动交易 v6.5 | {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ===\n")

# Step 1: Check portfolio - sell if TP/SL triggered
print("📊 [1/6] 检查持仓盈亏...")
result = skill_check_portfolio()
print(f"   持仓结果: {result.get('status')} | {result.get('message', '')}")
positions = result.get('positions', [])
print(f"   当前持仓数: {len(positions)}")

# Sell logic
ledger = load_ledger()
sold_any = False
for pos in positions:
    action = pos.get('action', 'hold')
    if action == 'SELL':
        token_id = pos['token_id']
        print(f"   🚨 触发{'止盈' if pos.get('pnl', 0) > 0 else '止损'}！尝试卖出 {token_id[:20]}...")
        sell_result = skill_sell(token_id)
        print(f"   卖出结果: {sell_result.get('status')} | {sell_result.get('message', '')}")
        if sell_result.get('status') == 'success':
            sold_any = True

# Reload ledger after sells
current_positions = [p['token_id'] for p in skill_check_portfolio().get('positions', [])]
current_count = len(current_positions)
print(f"   卖出后持仓数: {current_count}\n")

# Step 2: Radar scan
print("🛸 [2/6] 启动雷达扫描...")
radar = skill_radar(min_liquidity=5000, limit=50)
print(f"   雷达结果: {radar.get('status')} | {radar.get('message', '')}")
targets = radar.get('data', [])
print(f"   发现候选: {len(targets)} 个")

# Step 3: 24h cooldown check
cooldown = get_coldown_tokens()
print(f"\n⏱  [3/6] 24h冷却期检查...")
print(f"   冷却中: {len(cooldown)} 个")

# Step 4: Intelligence gathering & filter
print(f"\n🧠 [4/6] 情报调研 (扫描 {len(targets)} 个候选)...")
buy_candidates = []
for t in targets:
    token_id = t['token_id']
    if token_id in cooldown:
        print(f"   ⏳ 跳过冷却中: {t['title'][:50]}")
        continue
    if token_id in current_positions:
        print(f"   ⏳ 跳过已持仓: {t['title'][:50]}")
        continue
    
    # Quick intel
    intel = skill_multi_news_search(t['title'])
    score = intel.get('positive_score', 0)
    
    # Filter: score >= 2 or good title keywords
    is_good_title = any(kw in t['title'].lower() for kw in ['win', 'pass', 'approve', 'surge', 'yes'])
    if score >= 2 or (is_good_title and score >= 1):
        buy_candidates.append({**t, 'intel_score': score})
        print(f"   ✅ 买入候选: {t['title'][:50]} | 情报得分: {score}")
    else:
        print(f"   ❌ 过滤掉: {t['title'][:50]} | 得分: {score}")

# Step 5: Execute buys (only if < 3 positions and after sell settles)
print(f"\n💰 [5/6] 执行买入...")
needed = max(0, 3 - current_count)
print(f"   当前持仓: {current_count}, 需要买入: {needed}")
print(f"   符合条件候选: {len(buy_candidates)}")

if needed > 0 and buy_candidates:
    to_buy = buy_candidates[:needed]
    for candidate in to_buy:
        token_id = candidate['token_id']
        title = candidate['title']
        intel_score = candidate['intel_score']
        
        print(f"   买入: {title[:50]}...")
        buy_result = skill_auto_buy(token_id, 2.0, title)
        print(f"   结果: {buy_result.get('status')} | {buy_result.get('message', '')}")
        
        if buy_result.get('status') == 'success':
            add_to_cooldown(token_id)
            print(f"   ✅ 买入成功，进入24h冷却")
        elif buy_result.get('status') == 'skip':
            print(f"   ⏭ 跳过: {buy_result.get('reason', '')[:80]}")
        else:
            print(f"   ❌ 买入失败: {buy_result.get('message', '')[:80]}")
        
        time.sleep(2)  # Wait between trades
else:
    print(f"   持仓已满或无候选，跳过买入")

# Step 6: Final status
print(f"\n📊 [6/6] 最终状态...")
final = skill_check_portfolio()
print(f"   状态: {final.get('status')}")
print(f"   持仓数: {len(final.get('positions', []))}")
print(f"   总盈亏: ${final.get('total_pnl', 0)}")
for p in final.get('positions', []):
    print(f"   - {p['token_id'][:20]}... | 均价: ${p['avg_cost']} | 当前: ${p.get('current_price','?')} | ROI: {p.get('net_roi','?')}")

print("\n=== 完成 ===")
