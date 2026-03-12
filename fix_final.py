# -*- coding: utf-8 -*-
# Fix index.html: reverse article order, limit to 30, fix garbled text

with open('seo/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix garbled text patterns
content = content.replace('传奇技?</a>', '传奇技巧</a>')
content = content.replace('游戏技?</a>', '游戏技巧</a>')
content = content.replace('游戏环?</p>', '游戏环境</p>')
content = content.replace('技?</a>', '技巧</a>')
content = content.replace('�', '')

# Find the article-grid section and reverse cards
grid_start = content.find('<div class="article-grid">')
tips_start = content.find('<section class="tips-section">')

if grid_start > 0 and tips_start > 0:
    before = content[:grid_start]
    grid_section = content[grid_start:tips_start]
    after = content[tips_start:]
    
    # Split into individual cards
    cards = grid_section.split('<div class="article-card">')
    
    # Remove first empty element
    if cards and cards[0].strip() == '':
        cards = cards[1:]
    
    # Reverse to put newest first
    cards = cards[::-1]
    
    # Keep only first 30
    cards = cards[:30]
    
    # Reconstruct the grid section
    grid_section = '<div class="article-grid">' + '<div class="article-card">'.join(cards) + '</div></div></section>'
    
    # Combine
    content = before + grid_section + after

with open('seo/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done!')
