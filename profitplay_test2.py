import requests
from eth_account import Account
from eth_account.messages import encode_defunct

BASE = "http://profitplay-1066795472378.us-east1.run.app"
PRIVATE_KEY = "1a242c835cd309bef290b1547aadad03e71d1081e2fb23e90198a32fe10b9c7c"

acct = Account.from_key(PRIVATE_KEY)
print(f"Wallet: {acct.address}")

# Try different auth endpoints
for path in ["/auth/nonce", "/api/auth/nonce"]:
    r = requests.get(f"{BASE}{path}?address={acct.address}")
    print(f"{path}: {r.status_code}")

# Try login endpoints  
nonce_resp = requests.get(f"{BASE}/auth/nonce?address={acct.address}").json()
msg = encode_defunct(text=nonce_resp["message"])
sig = acct.sign_message(msg).signature.hex()

for path in ["/auth/login", "/api/auth/login"]:
    r = requests.post(f"{BASE}{path}", json={
        "address": acct.address,
        "message": nonce_resp["message"],
        "signature": f"0x{sig}"
    })
    print(f"{path}: {r.status_code} - {r.text[:200]}")
