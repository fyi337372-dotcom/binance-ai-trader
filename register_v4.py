import requests
import time
from Crypto.Hash import keccak
from eth_abi import encode
from eth_keys import keys

PRIVATE_KEY = '5b4124991d8e54193102f7f1aed7a19a66fd65216d87ccb74f73b80521e6390f'
WALLET = '0xee819cA1A51738C672Eb7215dAc6C6387753Eac9'

# Post new MoltBook post
API_KEY = 'moltbook_sk_BZfQSMzJ_meDq9Kz62gV0N9AiOzdm2bD'
content = """!claw_tech
```json
{
  "method": "register",
  "wallet": "0xee819cA1A51738C672Eb7215dAc6C6387753Eac9"
}
```
"""

r = requests.post('https://www.moltbook.com/api/v1/posts',
    headers={'Authorization': 'Bearer ' + API_KEY, 'Content-Type': 'application/json'},
    json={'title': 'Register v4', 'content': content, 'submolt': 'clawmarket-tech'})
print('Post:', r.status_code)
if r.status_code != 201:
    print(r.text)
    exit()

post_id = r.json()['post']['id']
print('Post ID:', post_id)

time.sleep(2)

# Get permit
r = requests.post('https://api.clawmarket.tech/register/prepare', json={'wallet': WALLET}, timeout=10)
permit = r.json()

def keccak256(data):
    k = keccak.new(digest_bits=256)
    if isinstance(data, str):
        data = data.encode()
    k.update(data)
    return k.digest()

domain = permit['permit']['domain']
msg = permit['permit']['message']

domain_encoded = encode(['bytes32', 'bytes32', 'uint256', 'address'],
    [keccak256(domain['name']), keccak256(domain['version']), domain['chainId'], domain['verifyingContract']])
domain_hash = keccak256(domain_encoded)

permit_encoded = encode(['address', 'address', 'uint256', 'uint256', 'uint256'],
    [msg['owner'], msg['spender'], int(msg['value']), int(msg['nonce']), int(msg['deadline'])])
message_hash = keccak256(permit_encoded)

final_hash = keccak256(b'\x19\x01' + domain_hash + message_hash)

priv_key = keys.PrivateKey(bytes.fromhex(PRIVATE_KEY))
sig = priv_key.sign_msg_hash(final_hash)
sig_hex = sig.to_bytes().hex()

v = int(sig_hex[-2:], 16)
r_sig = '0x' + sig_hex[2:66]
s_sig = '0x' + sig_hex[66:130]

print('v:', v)

# Try multiple times
for i in range(10):
    try:
        r2 = requests.post('https://api.clawmarket.tech/register', json={
            'post_id': post_id,
            'permit': {
                'owner': msg['owner'],
                'spender': msg['spender'],
                'value': msg['value'],
                'deadline': msg['deadline'],
                'v': v,
                'r': r_sig,
                's': s_sig
            }
        }, timeout=30)
        print(f'Attempt {i+1}: {r2.status_code}')
        if r2.status_code == 200:
            print('SUCCESS!', r2.text[:200])
            break
        elif r2.status_code != 502:
            print('Response:', r2.text[:100])
    except Exception as e:
        print(f'Attempt {i+1}: Error - {str(e)[:40]}')
    time.sleep(3)
