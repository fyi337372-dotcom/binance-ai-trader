import requests

# Check our agent stats
AGENT = '0xfab4Bf91C826C06e838220982d6B5cEdE1F282C1'

# Get holdings
r = requests.post('https://api.clawmarket.tech/keys/holdings', json={'agent': AGENT})
data = r.json()

print("=== OpenClaw Assistant Holdings ===")
total = 0
for h in data.get('holdings', []):
    price = float(h.get('average_price', 0))
    total += price
    print(f"{h.get('username')}: {price/1e18:.4f} ETH avg cost")

print(f"\nTotal investment: {total/1e18:.4f} ETH")
print("Holding keys: MartinClaw, Alea, OpenClaw Assistant")
