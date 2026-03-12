# -*- coding: utf-8 -*-
with open('seo/index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Add new article at beginning
new = '''
                <div class="article-card">
                    <span class="category">任务攻略</span>
                    <h3>传奇sf地图任务怎么完成？老玩家分享地图任务攻略和任务技巧</h3>
                    <p>传奇sf地图任务攻略，老玩家分享地图任务完成方法</p>
                    <div class="meta">更新时间：2026-03-05</div>
                    <a href="article/ditu-renwu.html" class="btn">阅读全文 →</a>
                </div>
'''

c = c.replace('<div class="article-grid">', '<div class="article-grid">' + new)

# Limit to 30
grid = c.find('<div class="article-grid">')
tips = c.find('<section class="tips-section">')
if grid > 0 and tips > 0:
    before = c[:grid+25]
    middle = c[grid+25:tips]
    after = c[tips:]
    cards = middle.split('<div class="article-card">')
    if cards and cards[0].strip() == '':
        cards = cards[1:]
    cards = cards[:30]
    middle = '<div class="article-grid">' + '<div class="article-card">'.join(cards)
    c = before + middle + after

with open('seo/index.html', 'w', encoding='utf-8') as f:
    f.write(c)

print('Done!')
