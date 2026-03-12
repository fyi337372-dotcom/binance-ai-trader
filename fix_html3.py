# -*- coding: utf-8 -*-
with open('seo/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix line 15: description content ending
# The issue is: ...成长?>  should be ...成长">
# Find and replace the exact pattern
content = content.replace('帮助新手快速成长?>', '帮助新手快速成长">')

# Fix line 17: keywords
# 传奇升级技?传奇装备获取 -> 传奇升级技巧,传奇装备获取
content = content.replace('传奇升级技?传奇装备获取', '传奇升级技巧,传奇装备获取')

# Fix search placeholder  
content = content.replace('搜索游戏攻略、技巧分�?..">', '搜索游戏攻略、技巧分享...">')

# Fix navigation - 技巧
content = content.replace('jiqiao.html">游戏技', 'jiqiao.html">游戏技巧')

# Fix category names that have �?
content = content.replace('<span class="category">技能攻�?/span>', '<span class="category">技能攻略</span>')
content = content.replace('<span class="category">开服指�?/span>', '<span class="category">开服指南</span>')
content = content.replace('<span class="category">理财攻略</span>', '<span class="category">理财攻略</span>')
content = content.replace('span>', 'span>')

# Fix article meta updates - �?? to proper date format
content = content.replace('更新时间�?026-', '更新时间：2026-')

# Fix button text
content = content.replace('�Ķ�ȫ�� �?', '阅读全文 →')

# Let me do a more aggressive cleanup - replace any remaining � with empty or fix patterns
import re

# Find any pattern like �?? and fix
content = re.sub(r'�\?+', '', content)

with open('seo/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed!")
