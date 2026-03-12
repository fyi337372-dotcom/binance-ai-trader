# -*- coding: utf-8 -*-
import re

with open('seo/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix all patterns where ? is incorrectly inserted

# Fix article descriptions - missing characters before ?>
# Pattern: ...赚?/p> -> ...赚钱</p>
content = content.replace('赚?/p>', '赚钱</p>')
content = content.replace('满?/p>', '满级</p>')
content = content.replace('特?/p>', '特效</p>')
content = content.replace('装?/p>', '装备</p>')
content = content.replace('级?/p>', '升级</p>')
content = content.replace('巧?/p>', '技巧</p>')
content = content.replace('级?/h3>', '等级</h3>')

# Fix meta updates - missing : before date
content = content.replace('更新时间?026-', '更新时间：2026-')

# Fix button text
content = content.replace('>阅读全文 ?/a>', '>阅读全文 →</a>')

# Fix navigation menu
content = content.replace('jiqiao.html">游戏技', 'jiqiao.html">游戏技巧')

# Fix category spans
content = content.replace('<span class="category">技能攻�?/span>', '<span class="category">技能攻略</span>')
content = content.replace('<span class="category">开服指�?/span>', '<span class="category">开服指南</span>')
content = content.replace('<span class="category">技术教�?/span>', '<span class="category">技术教程</span>')

# Fix any remaining � followed by ? patterns
content = re.sub(r'�\?', '', content)
content = re.sub(r'�+', '', content)

# Fix patterns like "理财攻略</span>" that might have issues
# Fix description issues in articles
content = content.replace('的打?', '的打金')

# More description fixes
content = content.replace('你选择最强?</p>', '你选择最强特戒</p>')
content = content.replace('帮你打到好装?</p>', '帮你打到好装备</p>')
content = content.replace('帮你打造更强角?</p>', '帮你打造更强角色</p>')
content = content.replace('帮你打造炫酷外?</p>', '帮你打造炫酷外观</p>')
content = content.replace('帮你安心买?</p>', '帮你安心买卖</p>')
content = content.replace('帮你强化装备更顺?</p>', '帮你强化装备更顺利</p>')
content = content.replace('帮你获取顶级武?</p>', '帮你获取顶级武器</p>')
content = content.replace('帮你学会强力技?</p>', '帮你学会强力技能</p>')
content = content.replace('帮你安心交?</p>', '帮你安心交易</p>')
content = content.replace('帮你通关魔龙血?</p>', '帮你通关魔龙血域</p>')
content = content.replace('帮你打到高级技能书</p>', '帮你打到高级技能书</p>')
content = content.replace('帮你成为服务器最靓的?</p>', '帮你成为服务器最靓的仔</p>')
content = content.replace('帮你获得最强坐?</p>', '帮你获得最强坐骑</p>')
content = content.replace('帮你打造炫酷外?</p>', '帮你打造炫酷外观</p>')

# Fix h3 titles that got truncated
content = content.replace('的最强特?</h3>', '的最强特戒</h3>')
content = content.replace('刷新时间及地?</h3>', '刷新时间及地点</h3>')
content = content.replace('召唤骷髅技能升级攻?</h3>', '召唤骷髅技能升级攻略</h3>')
content = content.replace('羽翼升级材料获取攻?</h3>', '羽翼升级材料获取攻略</h3>')
content = content.replace('线下交易防骗技?</h3>', '线下交易防骗技巧</h3>')
content = content.replace('祝福油获取攻略和使用技?</h3>', '祝福油获取攻略和使用技巧</h3>')
content = content.replace('武器获取攻略和属性介?</h3>', '武器获取攻略和属性介绍</h3>')
content = content.replace('技能书获取途径和打书技?</h3>', '技能书获取途径和打书技巧</h3>')
content = content.replace('元宝交易防骗技?</h3>', '元宝交易防骗技巧</h3>')
content = content.replace('坐骑系统玩法和属性加?</h3>', '坐骑系统玩法和属性加成</h3>')
content = content.replace('翅膀升级技巧和外观展示</h3>', '翅膀升级技巧和外观展示</h3>')

# Fix utility section
content = content.replace('实用技�?>', '实用技巧</h2>')
content = content.replace('快捷键使�?</h4>', '快捷键使用</h4>')
content = content.replace('自动拾取设置</h4>', '自动拾取设置</h4>')
content = content.replace('交易防骗指南</h4>', '交易防骗指南</h4>')
content = content.replace('背包整理技�?</h4>', '背包整理技巧</h4>')

# Fix footer
content = content.replace('游戏资讯</a> |', '游戏资讯</a> |')
content = content.replace('分享游戏乐趣、交流游戏心�?</p>', '分享游戏乐趣、交流游戏心得</p>')

# Fix search placeholder
content = content.replace('搜索游戏攻略、技巧分?</input>', '搜索游戏攻略、技巧分享...">')

with open('seo/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Comprehensive fixes applied!")
