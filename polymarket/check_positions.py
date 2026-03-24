import json
with open('ledger.json') as f:
    ledger = json.load(f)
print('Type:', type(ledger))
if isinstance(ledger, list):
    print('Positions:', len(ledger))
    for p in ledger:
        q = p.get('question', '')[:50]
        qty = p.get('qty') or 0
        avg = p.get('avg_cost') or 0
        cur = p.get('current_price') or 0
        pnl = p.get('pnl_pct') or 0
        print(f'  Q: {q}')
        print(f'    qty={qty} avg={avg:.4f} cur={cur:.4f} PnL={pnl:.1%}')
