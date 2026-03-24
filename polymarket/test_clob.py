import sys
sys.path.insert(0, 'C:/Users/Administrator/.openclaw/workspace')

from skills import get_clob_market

# Test the tightest spread markets
test_cids = [
    '0xbb57ccf5853a85487bc3d83d04d669310d28c6c810758953b9d9b91d1aee89d2',  # bitcoin hit 1m before gta vi
    '0x86bfb53af7250a40928975c551d12c185b762fa4ce0b40c6a64a50c946d72587',  # gop senate 2026
    '0x16c63b7cc37f012b9f59ee164ec03877914c701d06d48291ae8d6fc08a088b0d',  # balance power
]

for cid in test_cids:
    try:
        p = get_clob_market(cid)
        print(f'CID: {cid[:20]}...')
        print(f'  Yes: {p.get("yes_price")}, No: {p.get("no_price")}')
        print(f'  Outcome: {p.get("outcome")}')
    except Exception as e:
        print(f'Error: {e}')
