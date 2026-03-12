# -*- coding: utf-8 -*-
with open('seo/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix og:title - content="传奇游戏攻略_传奇技巧分?> 
content = content.replace('og:title" content="传奇游戏攻略_传奇技巧分?>', 'og:title" content="传奇游戏攻略_传奇技巧分享"')

# Also fix navigation link
content = content.replace('jiqiao.html">游戏技</a>', 'jiqiao.html">游戏技巧</a>')

# Check and fix footer
content = content.replace('游戏资讯</a> |', '游戏资讯</a> |')

with open('seo/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed og:title and nav!")
