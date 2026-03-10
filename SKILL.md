{
  "name": "binance-trading-signal",
  "version": "1.0.0",
  "description": "Binance Trading Signal Assistant - AI-powered technical analysis tool for cryptocurrency trading pairs",
  "author": "AI Trading Team",
  "license": "MIT",
  "homepage": "https://github.com/fyi337372-dotcom/binance-ai-trader",
  "keywords": ["binance", "trading", "signal", "crypto", "technical-analysis", "RSI", "MA"],
  "triggers": [
    "查币价",
    "XXX现在能买吗",
    "XXX走势如何",
    "交易信号",
    "技术分析",
    "推荐个币",
    "币安价格",
    "check price",
    "trading signal",
    "technical analysis"
  ],
  "endpoints": {
    "base": "https://api.binance.com/api/v3",
    "ticker": "/ticker/24hr",
    "klines": "/klines"
  },
  "parameters": {
    "symbol": {
      "type": "string",
      "required": true,
      "description": "Trading pair symbol (e.g., BTC, ETH, PEPE)",
      "autoSuffix": "USDT"
    }
  },
  "indicators": {
    "MA20": {
      "name": "20-hour Moving Average",
      "period": 20,
      "description": "Average of last 20 1-hour candles. Price > MA20 = bullish, Price < MA20 = bearish"
    },
    "RSI": {
      "name": "Relative Strength Index",
      "period": 14,
      "range": "0-100",
      "description": ">70 overbought (potential sell), <30 oversold (potential buy), >50 bullish zone, <50 bearish zone"
    }
  },
  "rating": {
    "strong_buy": {"score": ">=2", "label": "强烈买入 📈📈"},
    "buy": {"score": "1", "label": "轻度买入 📈"},
    "hold": {"score": "0", "label": "观望 ⚪"},
    "sell": {"score": "-1", "label": "轻度卖出 🔴"},
    "strong_sell": {"score": "<=-2", "label": "强烈卖出 📉📉"}
  },
  "response": {
    "format": "markdown",
    "sections": [
      "price_info",
      "technical_indicators", 
      "signals",
      "recommendation",
      "trading_link"
    ]
  },
  "example": {
    "input": "BTC现在能买吗",
    "output": {
      "symbol": "BTC/USDT",
      "price": "$71,255.43",
      "change_24h": "-2.04%",
      "ma20": "$71,500",
      "rsi": "45.0",
      "signals": ["RSI中性", "跌破MA20"],
      "recommendation": "观望 ⚪",
      "link": "https://www.binance.com/zh-CN/trade/BTC_USDT"
    }
  },
  "notes": [
    "Uses public Binance API - no API key required",
    "All prices in USDT",
    "For educational purposes only",
    "Not financial advice"
  ]
}
