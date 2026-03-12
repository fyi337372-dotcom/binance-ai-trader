# -*- coding: utf-8 -*-
with open('seo/index.html', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('传奇技?</a>', '传奇技巧</a>')
c = c.replace('游戏技?</a>', '游戏技巧</a>')

new_article = '''
                <div class="article-card">
                    <span class="category">武器攻略</span>
                    <h3>传奇sf炼狱怎么获得？老玩家分享炼狱武器属性和获取途径</h3>
                    <p>传奇sf炼狱获取攻略，老玩家分享炼狱武器属性</p>
                    <div class="meta">更新时间：2026-03-05</div>
                    <a href="article/lianyu-wuqi.html" class="btn">阅读全文 →</a>
                </div>
'''

c = c.replace('<div class="article-grid">', '<div class="article-grid">' + new_article)

grid_start = c.find('<div class="article-grid">')
tips_start = c.find('<section class="tips-section">')

if grid_start > 0 and tips_start > 0:
    before = c[:grid_start + 25]
    grid = c[grid_start + 25:tips_start]
    after = c[tips_start:]
    
    cards = grid.split('<div class="article-card">')
    if cards and cards[0].strip() == '':
        cards = cards[1:]
    
    cards = cards[:30]
    
    grid = '<div class="article-grid">' + '<div class="article-card">'.join(cards)
    c = before + grid + after

with open('seo/index.html', 'w', encoding='utf-8') as f:
    f.write(c)

print('Done!')
