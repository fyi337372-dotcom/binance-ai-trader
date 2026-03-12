# -*- coding: utf-8 -*-
with open('seo/index.html', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('传奇技?</a>', '传奇技巧</a>')
c = c.replace('游戏技?</a>', '游戏技巧</a>')

new = '''
                <div class="article-card">
                    <span class="category">坐骑攻略</span>
                    <h3>传奇sf坐骑系统攻略 老玩家分享坐骑获取和培养方法</h3>
                    <p>传奇sf坐骑系统攻略，老玩家分享坐骑获取和培养方法</p>
                    <div class="meta">更新时间：2026-03-06</div>
                    <a href="article/zuoji-xitong.html" class="btn">阅读全文 →</a>
                </div>
'''

c = c.replace('<div class="article-grid">', '<div class="article-grid">' + new)

gs = c.find('<div class="article-grid">')
ts = c.find('<section class="tips-section">')

if gs > 0 and ts > 0:
    before = c[:gs + 25]
    grid = c[gs + 25:ts]
    after = c[ts:]
    
    cards = grid.split('<div class="article-card">')
    if cards and cards[0].strip() == '':
        cards = cards[1:]
    
    cards = cards[:30]
    
    grid = '<div class="article-grid"><div class="article-card">'.join(cards)
    c = before + grid + after

with open('seo/index.html', 'w', encoding='utf-8') as f:
    f.write(c)

print('Done!')
