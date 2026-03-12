# -*- coding: utf-8 -*-
import re

with open('seo/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix all the garbled patterns systematically

# h3 titles with missing ending characters
content = content.replace('属性加?/h3>', '属性加成</h3>')
content = content.replace('技能升级攻?/h3>', '技能升级攻略</h3>')
content = content.replace('获取途径和价?/h3>', '获取途径和价格</h3>')
content = content.replace('最强特?/h3>', '最强特戒</h3>')
content = content.replace('刷新时间及地?/h3>', '刷新时间及地点</h3>')
content = content.replace('召唤骷髅技能升级攻?/h3>', '召唤骷髅技能升级攻略</h3>')
content = content.replace('羽翼升级材料获取攻?/h3>', '羽翼升级材料获取攻略</h3>')
content = content.replace('线下交易防骗技?/h3>', '线下交易防骗技巧</h3>')
content = content.replace('祝福油获取攻略和使用技?/h3>', '祝福油获取攻略和使用技巧</h3>')
content = content.replace('武器获取攻略和属性介?/h3>', '武器获取攻略和属性介绍</h3>')
content = content.replace('技能书获取途径和打书技?/h3>', '技能书获取途径和打书技巧</h3>')
content = content.replace('元宝交易防骗技?/h3>', '元宝交易防骗技巧</h3>')
content = content.replace('坐骑系统玩法和属性加?/h3>', '坐骑系统玩法和属性加成</h3>')
content = content.replace('学强力技?/h3>', '学强力技能</h3>')
content = content.replace('日入百?/p>', '日入百万</p>')
content = content.replace('升级技?/h3>', '升级技巧</h3>')
content = content.replace('PK走位技巧分享！老玩家分享战士野外单挑必学操?/h3>', 'PK走位技巧分享！老玩家分享战士野外单挑必学操作</h3>')
content = content.replace('打宝技?/h3>', '打宝技巧</h3>')

# p descriptions with missing characters
content = content.replace('最强坐?/p>', '最强坐骑</p>')
content = content.replace('炫酷外?/p>', '炫酷外观</p>')
content = content.replace('强力技?/p>', '强力技能</p>')
content = content.replace('好装?/p>', '好装备</p>')
content = content.replace('更强角?/p>', '更强角色</p>')
content = content.replace('安心买?/p>', '安心买卖</p>')
content = content.replace('更顺?/p>', '更顺利</p>')
content = content.replace('顶级武?/p>', '顶级武器</p>')
content = content.replace('安心交?/p>', '安心交易</p>')
content = content.replace('魔龙血?/p>', '魔龙血域</p>')
content = content.replace('最靓的?/p>', '最靓的仔</p>')
content = content.replace('外?/p>', '外观</p>')
content = content.replace('最强特戒</p>', '最强特戒</p>')

# Fix category spans
content = content.replace('<span class="category">技能攻?/span>', '<span class="category">技能攻略</span>')
content = content.replace('<span class="category">开服指?/span>', '<span class="category">开服指南</span>')
content = content.replace('<span class="category">技术教?/span>', '<span class="category">技术教程</span>')

# Fix h3 title that has question mark issues
content = content.replace('攻?/h3>', '攻略</h3>')

# More h3 fixes
content = content.replace('pk走位技巧分享！老玩家分享战士野外单挑必学操?/h3>', 'pk走位技巧分享！老玩家分享战士野外单挑必学操作</h3>')

# Additional patterns
content = content.replace('打宝技?</p>', '打宝技巧</p>')

with open('seo/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed!")
