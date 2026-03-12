# -*- coding: utf-8 -*-
with open('seo/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix garbled text
content = content.replace('传奇技?</a>', '传奇技巧</a>')
content = content.replace('游戏技?</a>', '游戏技巧</a>')
content = content.replace('技?</a>', '技巧</a>')
content = content.replace('�', '')

# Find article section
start_marker = '<div class="article-grid">'
end_marker = '</div></div></section>'

start = content.find(start_marker)
end = content.find(end_marker)

if start > 0 and end > 0:
    article_section = content[start:end+len(end_marker)]
    
    # Split into cards
    cards = article_section.split('<div class="article-card">')
    
    # Remove first empty element
    if cards[0].strip() == '':
        cards = cards[1:]
    
    print(f'Found {len(cards)} cards')
    
    # Reverse order - newest first
    cards = cards[::-1]
    
    # Keep only first 30
    cards = cards[:30]
    
    # Reconstruct
    new_section = '<div class="article-grid">' + '<div class="article-card">'.join(cards)
    
    # Replace in content
    content = content[:start] + new_section + content[end+len(end_marker):]

with open('seo/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done!')
