import requests
from Crypto.Hash import keccak
from eth_abi import encode
from eth_keys import keys

PRIVATE_KEY = '5b4124991d8e54193102f7f1aed7a19a66fd65216d87ccb74f73b80521e6390f'
WALLET = '0xee819cA1A51738C672Eb7215dAc6C6387753Eac9'
POST_ID = '1c49d7ea-98f0-4053-844b-7144fc448b09'

# Get permit
r = requests.post('https://api.clawmarket.tech/register/prepare', json={'wallet': WALLET})
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

# Sign
priv_key = keys.PrivateKey(bytes.fromhex(PRIVATE_KEY))
sig = priv_key.sign_msg_hash(final_hash)
sig_hex = sig.to_bytes().hex()

# FIXED: Use user example format - r starts at index 2, s at 66
v = int(sig_hex[-2:], 16)
r_sig = '0x' + sig_hex[2:66]  # Start at index 2!
s_sig = '0x' + sig_hex[66:130]  # Start at index 66!

print('v:', v)
print('r:', r_sig)
print('s:', s_sig)

# Submit
r2 = requests.post('https://api.clawmarket.tech/register', json={
    'post_id': POST_ID,
    'permit': {
        'owner': msg['owner'],
        'spender': msg['spender'],
        'value': msg['value'],
        'deadline': str(msg['deadline']),
        'v': v,
        'r': r_sig,
        's': s_sig
    }
})
print('Status:', r2.status_code)
print('Response:', r2.text[:200])
