#!/usr/bin/env python3
"""
Polymarket market scanner - fixed version.
Scans gamma API for active markets with tight spreads.
"""
import sys, os, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import requests, json
from datetime import datetime

API = 'https://gamma-api.polymarket.com'

def get_all_markets(limit=500):
    # IMPORTANT: closed/archived must be in URL string, not params dict
    url = f'{API}/markets?limit={limit}&closed=false&archived=false'
    r = requests.get(url, timeout=30)
    r.raise_for_status()
    return r.json()

def filter_by_leverage(markets):
    """Skip leverage/margin tokens"""
    filtered = []
    skip_words = ['lev', 'leverage', '2x', '3x', '5x', '10x', 'margin', 'long', 'short']
    for m in markets:
        q = m.get('question', '').lower()
        if m.get('spread', 0) > 0.15 and any(w in q for w in skip_words):
            continue
        filtered.append(m)
    return filtered

def scan(limit=500, min_vol=0, max_spread=0.7, min_price=0.01):
    markets = get_all_markets(limit=limit)
    print(f'Fetched {len(markets)} markets')
    
    candidates = []
    for m in markets:
        # Filter by accepting orders
        if not m.get('acceptingOrders', False):
            continue
        
        op = m.get('outcomePrices', '')
        if not op:
            continue
        
        try:
            if op.startswith('['):
                raw = json.loads(op)
                prices = [float(p) for p in raw]
            else:
                prices = [float(p) for p in op.split(',')]
        except:
            continue
        
        if len(prices) < 2:
            continue
        
        min_p = min(prices)
        max_p = max(prices)
        
        # Spread filter
        if max_p > 0 and (max_p - min_p) / max_p > max_spread:
            continue
        
        # Min price filter
        if min_p < min_price:
            continue
        
        vol = float(m.get('volume24hr', 0) or 0)
        if vol < min_vol:
            continue
        
        spread = (max_p - min_p) / max_p if max_p > 0 else 1
        slug = m.get('slug', '')
        candidates.append({
            'question': m.get('question', ''),
            'condition_id': m.get('conditionId', ''),
            'slug': slug,
            'spread': spread,
            'min_price': min_p,
            'max_price': max_p,
            'prices': prices,
            'vol': vol,
            'vol_all': float(m.get('volume', 0) or 0),
        })
    
    print(f'After filters: {len(candidates)} candidates')
    candidates = filter_by_leverage(candidates)
    print(f'After leverage filter: {len(candidates)} candidates')
    
    # Sort by volume
    candidates.sort(key=lambda x: x['vol'], reverse=True)
    return candidates

if __name__ == '__main__':
    candidates = scan(min_vol=100, max_spread=0.7)
    print(f'\nTop candidates by 24h volume:')
    for i, m in enumerate(candidates[:20]):
        print(f'\n[{i+1}] {m["question"][:80]}')
        print(f'  Spread: {m["spread"]:.1%} | 24h Vol: ${m["vol"]:.0f} | Total Vol: ${m["vol_all"]:.0f}')
        print(f'  Prices: {[f"{p:.3f}" for p in m["prices"]]}')
        print(f'  URL: https://polymarket.com/event/{m["slug"]}')
        print(f'  CID: {m["condition_id"]}')
