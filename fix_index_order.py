# -*- coding: utf-8 -*-
import re

# Read index.html
with open('seo/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix garbled patterns
content = content.replace('传奇技?</a>', '传奇技巧</a>')
content = content.replace('游戏技?</a>', '游戏技巧</a>')
content = content.replace('技?</a>', '技巧</a>')
content = content.replace('�', '')

# Find the article cards section and reverse the order
# The articles are in reverse order currently, we need to flip them

# Find the article list section
article_start = content.find('<div class="article-grid">')
article_end = content.find('</div>', article_start) + 6

# Extract the article cards
article_section = content[article_start:article_end]
# Split into individual cards
cards = article_section.split('</div>\n                \n                <div class="article-card">')

# Reverse the order so newest is first
cards = cards[::-1]

# Take only first 30
cards = cards[:30]

# Reconstruct
new_article_section = '</div>\n                \n                <div class="article-card">'.join(cards) + '</div>'

content = content[:article_start] + new_article_section + content[article_end:]

# Save
with open('seo/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done!")
