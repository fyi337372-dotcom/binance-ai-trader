import requests
from eth_account import Account
from eth_account.messages import encode_defunct
from web3 import Web3
import time

BASE = "http://profitplay-1066795472378.us-east1.run.app"
PRIVATE_KEY = "1a242c835cd309bef290b1547aadad03e71d1081e2fb23e90198a32fe10b9c7c"

acct = Account.from_key(PRIVATE_KEY)
print(f"Wallet: {acct.address}")

# 1. Get nonce
print("\n1. Getting nonce...")
nonce_resp = requests.get(f"{BASE}/auth/nonce?address={acct.address}").json()
print(f"Nonce: {nonce_resp}")

# 2. Sign message
print("\n2. Signing message...")
msg = encode_defunct(text=nonce_resp["message"])
sig = acct.sign_message(msg).signature.hex()
print(f"Signature: {sig}")

# 3. Login
print("\n3. Logging in...")
login_resp = requests.post(f"{BASE}/auth/login", json={
    "address": acct.address,
    "message": nonce_resp["message"],
    "signature": f"0x{sig}"
})
print(f"Status: {login_resp.status_code}")
print(f"Response: {login_resp.text}")
login = login_resp.json()
print(f"Login response: {login}")

if "accessToken" in login:
    TOKEN = login["accessToken"]
    headers = {"Authorization": f"Bearer {TOKEN}"}
    print("\n✅ Authentication successful!")
    
    # 4. Check account status
    print("\n4. Checking account...")
    account = requests.get(f"{BASE}/api/account", headers=headers).json()
    print(f"Account: {account}")
    
    # 5. Check platform wallet for deposit
    print("\n5. Checking platform wallet...")
    platform_addr = requests.get(f"{BASE}/api/platform").json()["platformWallet"]
    print(f"Platform wallet: {platform_addr}")
    
    # Check balance on chain
    w3 = Web3(Web3.HTTPProvider('https://base-mainnet.public.blastapi.io'))
    bal = w3.eth.get_balance(acct.address)
    print(f"On-chain balance: {w3.from_wei(bal, 'ether')} ETH")
    
    # For testing, we need to deposit. But we need a tx hash.
    # Since the user already sent ETH, we can try to call deposit API
    print("\nNote: To deposit, we need the tx hash of the transfer to platform wallet")
    print("Please transfer ETH to platform wallet and provide tx hash")
else:
    print(f"\n❌ Login failed: {login}")
