import requests

r = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,solana,toncoin&vs_currencies=usd&include_24hr_change=true')
data = r.json()

print("=== Crypto Prices ===")
for coin, info in data.items():
    change = info.get('usd_24h_change', 0)
    print(f"{coin}: ${info['usd']} ({change:.2f}%)")

# Check if any are down significantly - potential buy opportunity
print("\n=== Potential Opportunities ===")
for coin, info in data.items():
    change = info.get('usd_24h_change', 0)
    if change < -3:
        print(f"{coin} is down {abs(change)}% - could be a buy signal")
    elif change > 5:
        print(f"{coin} is up {change}% - risky to buy now")
