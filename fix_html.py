# -*- coding: utf-8 -*-
with open('seo/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the description line - remove the trailing ?>
content = content.replace('帮助新手快速成长?>', '帮助新手快速成长">')

# Check keywords line
content = content.replace('传奇技巧?>', '传奇技巧">')

# More fixes for other corrupted meta tags
content = content.replace('传奇技巧分�?>', '传奇技巧分享">')

# Fix navigation items  
content = content.replace('jiqiao.html">游戏技�?/a>', 'jiqiao.html">游戏技巧</a>')

# Fix search placeholder
content = content.replace('搜索游戏攻略、技巧分�?..">', '搜索游戏攻略、技巧分享...</a>')

# Fix more �?? patterns  
content = content.replace('�', '')

# Also need to fix article links and buttons
content = content.replace('�', '')

with open('seo/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed!")
