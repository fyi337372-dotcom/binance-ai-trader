# -*- coding: utf-8 -*-
import re

with open('seo/index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Fix garbled text
c = c.replace('传奇技?</a>', '传奇技巧</a>')
c = c.replace('游戏环?</p>', '游戏环境</p>')
c = c.replace('游戏技?</a>', '游戏技巧</a>')
c = c.replace('�', '')

# Find article-grid section
grid_start = c.find('<div class="article-grid">')
tips_start = c.find('<section class="tips-section">')

print(f'Grid: {grid_start}, Tips: {tips_start}')

if grid_start > 0 and tips_start > 0:
    before = c[:grid_start + 25]  # len('<div class="article-grid">')
    after = c[tips_start:]
    middle = c[grid_start + 25:tips_start]
    
    # Split into individual cards
    parts = middle.split('<div class="article-card">')
    if parts and parts[0].strip() == '':
        parts = parts[1:]
    
    print(f'Card parts: {len(parts)}')
    
    # Reverse and take 30
    parts = parts[::-1][:30]
    
    # Reconstruct
    new_middle = '<div class="article-card">'.join(parts)
    c = before + new_middle + after

with open('seo/index.html', 'w', encoding='utf-8') as f:
    f.write(c)

print('Done!')
