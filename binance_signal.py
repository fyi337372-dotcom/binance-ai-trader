# -*- coding: utf-8 -*-
"""
Binance AI Trading Signal Tool
币安智能交易信号工具 - Python版
"""

import requests

BASE_URL = 'https://api.binance.com/api/v3'

def get_24hr_stats(symbol):
    """获取24小时行情统计"""
    r = requests.get(f'{BASE_URL}/ticker/24hr', params={'symbol': symbol})
    data = r.json()
    return {
        'price': float(data['lastPrice']),
        'change_pct': float(data['priceChangePercent']),
        'high': float(data['highPrice']),
        'low': float(data['lowPrice']),
        'volume': float(data['quoteVolume']),
    }

def get_klines(symbol, interval='1h', limit=60):
    """获取K线数据"""
    r = requests.get(f'{BASE_URL}/klines', params={
        'symbol': symbol, 'interval': interval, 'limit': limit
    })
    return [float(k[4]) for k in r.json()]

def calculate_ma(prices, period=20):
    """计算移动平均线"""
    if len(prices) < period:
        return prices[-1]
    return sum(prices[-period:]) / period

def calculate_rsi(prices, period=14):
    """计算RSI指标"""
    deltas = [prices[i] - prices[i-1] for i in range(1, len(prices))]
    gains = [d if d > 0 else 0 for d in deltas]
    losses = [-d if d < 0 else 0 for d in deltas]
    
    if len(gains) < period:
        return 50
    
    avg_gain = sum(gains[-period:]) / period
    avg_loss = sum(losses[-period:]) / period
    
    if avg_loss == 0:
        return 100
    return 100 - (100 / (1 + avg_gain / avg_loss))

def analyze(symbol):
    """分析币种并返回信号"""
    if not symbol.endswith('USDT'):
        symbol = symbol + 'USDT'
    
    stats = get_24hr_stats(symbol)
    closes = get_klines(symbol)
    ma20 = calculate_ma(closes, 20)
    rsi = calculate_rsi(closes)
    
    # 信号评分
    score = 0
    signals = []
    
    if rsi < 30:
        signals.append('RSI超卖-买入')
        score += 2
    elif rsi > 70:
        signals.append('RSI超买-卖出')
        score -= 2
    else:
        signals.append(f'RSI中性({rsi:.0f})')
    
    if stats['price'] > ma20:
        signals.append('站上MA20-支撑')
        score += 1
    else:
        signals.append('跌破MA20-压力')
        score -= 1
    
    if stats['change_pct'] < -3:
        signals.append('超跌')
        score += 1
    elif stats['change_pct'] > 3:
        signals.append('超涨')
        score -= 1
    
    # 建议
    if score >= 2:
        rec = '强烈买入'
    elif score == 1:
        rec = '轻度买入'
    elif score == -1:
        rec = '轻度卖出'
    elif score <= -2:
        rec = '强烈卖出'
    else:
        rec = '观望'
    
    return {
        'symbol': symbol,
        'price': stats['price'],
        'change_pct': stats['change_pct'],
        'high': stats['high'],
        'low': stats['low'],
        'volume': stats['volume'],
        'ma20': ma20,
        'rsi': rsi,
        'signals': signals,
        'recommendation': rec,
        'score': score
    }

def format_output(result):
    """格式化输出"""
    coin = result['symbol'].replace('USDT', '')
    return f"""
====================================================
            {result['symbol']} 实时分析
====================================================

  **当前价格**    ${result['price']:.4f}
  24h涨跌       {result['change_pct']:+.2f}%
  24h最高       ${result['high']:.4f}
  24h最低       ${result['low']:.4f}
  24h交易额     ${result['volume']/1e6:.1f}M美元

  -----------------------------------------------

  📊 技术指标

  MA20 (20小时均线): ${result['ma20']:.2f}
     → 过去20根1小时K线的平均值
       价格>MA20表示多头，<MA20表示空头

  RSI (相对强弱指标): {result['rsi']:.1f}
     → 0-100，数值越高越强势
       >70超买可能跌，<30超卖可能涨
       >50处于多头区域，<50处于空头区域

  -----------------------------------------------

  📋 信号判断
{chr(10).join(['       • ' + s for s in result['signals']])}

  -----------------------------------------------

  🎯 综合建议: {result['recommendation']}

====================================================
  🔗 立即购买: https://www.binance.com/zh-CN/trade/{coin}_USDT
====================================================
"""

def main():
    import sys
    symbol = input('请输入币种 (如 BTC, ETH, PEPE): ').strip().upper()
    if not symbol:
        print('请输入币种名称')
        return
    
    try:
        result = analyze(symbol)
        print(format_output(result))
    except Exception as e:
        print(f'获取数据失败: {e}')

if __name__ == '__main__':
    main()
