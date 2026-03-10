from web3 import Web3

w3 = Web3(Web3.HTTPProvider('https://base-mainnet.public.blastapi.io'))
addr = '0x17c4465A00D3Be10e98f8DF5282cb26DE8AaD5BD'
bal = w3.eth.get_balance(addr)
print(f'Balance: {w3.from_wei(bal, "ether")} ETH')
