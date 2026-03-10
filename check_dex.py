import requests

# Get trending tokens on Solana
sol_trending = requests.get('https://api.dexscreener.com/latest/dex/tokens/solana').json()
print('=== Solana Trending ===')
pairs = sol_trending.get('pairs', [])[:5]
for p in pairs:
    symbol = p['baseToken']['symbol']
    price = p.get('priceUsd', 'N/A')
    vol = p.get('volume24h', 'N/A')
    print(f'{symbol}: {price} (Vol: {vol})')

print()

# Get trending on BSC  
bsc = requests.get('https://api.dexscreener.com/latest/dex/tokens/bsc').json()
print('=== BSC Trending ===')
pairs = bsc.get('pairs', [])[:5]
for p in pairs:
    symbol = p['baseToken']['symbol']
    price = p.get('priceUsd', 'N/A')
    vol = p.get('volume24h', 'N/A')
    print(f'{symbol}: {price} (Vol: {vol})')
