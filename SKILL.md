# Binance Trading Signal Skill

A skill that provides AI-powered trading signals for Binance trading pairs using technical analysis.

## Description

This skill analyzes cryptocurrency trading pairs on Binance and provides intelligent trading signals based on technical indicators including MA20 and RSI.

## Triggers

Use this skill when user asks:
- "查询XXX币价"
- "XXX现在能买吗"
- "XXX技术分析"
- "XXX走势如何"
- "推荐个币"
- "trading signal"
- "交易信号"
- Check cryptocurrency price/analysis

## Actions

1. **Price Query** - Get current price for any Binance trading pair
2. **Technical Analysis** - Calculate MA20, RSI indicators
3. **Signal Generation** - Generate buy/sell/hold recommendations
4. **Top Coins** - List trending coins by volume

## Parameters

- `symbol` (required): Trading pair symbol (e.g., "BTC", "ETH", "PEPE")
- Auto-add "USDT" suffix if not present

## Response Format

Provide formatted output with:
- Current price with 24h change
- Technical indicators (MA20, RSI) with explanations
- Signal judgment
- Trading recommendation
- Binance trading link

## Technical Indicators

### MA20 (20-hour Moving Average)
- Average of last 20 1-hour candles
- Price > MA20 = bullish
- Price < MA20 = bearish

### RSI (Relative Strength Index)
- Range 0-100
- >70 = overbought (potential sell)
- <30 = oversold (potential buy)
- >50 = bullish zone
- <50 = bearish zone

## Rating System

| Score | Recommendation |
|-------|----------------|
| ≥2 | Strong Buy |
| 1 | Buy |
| 0 | Hold |
| -1 | Sell |
| ≤-2 | Strong Sell |

## Example

**Input**: "BTC现在能买吗"

**Output**:
```
BTC/USDT 实时分析
当前价格: $71,255.43
24h涨跌: -2.04%
...

📊 技术指标
MA20: $71,500 (20小时均线)
RSI: 45.0

🎯 综合建议: 观望
🔗 购买: https://www.binance.com/zh-CN/trade/BTC_USDT
```

## Notes

- Uses public Binance API (no API key required)
- All prices in USDT
- For educational purposes only
- Not financial advice
