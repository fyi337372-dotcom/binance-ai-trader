import requests

# Get key prices from leaderboard
r = requests.post('https://api.clawmarket.tech/keys', json={'limit': 20})
data = r.json()

print("=== Key Prices (CP) ===")
for k in data.get('keys', [])[:10]:
    addr = k.get('address', '')
    # Get key info
    r2 = requests.post('https://api.clawmarket.tech/keys', json={'address': addr})
    info = r2.json()
    if info.get('keys'):
        key_info = info['keys'][0]
        print(f"{key_info.get('username')}: {key_info.get('key_price')} CP")
