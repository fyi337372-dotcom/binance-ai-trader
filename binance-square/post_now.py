# -*- coding: utf-8 -*-
import requests
import random
import sys

API_KEY = 'ead750e55b1b4a0c8992766992df8e12'

topics = [
    '币圈老韭菜的自我修养：别想着一夜暴富',
    '囤币党的心路历程',
    '今天又亏了，但我不慌',
    '币圈生存法则：第一条不要听群里的',
    '合约爆仓教会我的事',
    '从爆仓到稳定盈利，我做对了什么',
    '币圈最可怕的不是暴跌，而是',
    '为什么我永远不满仓',
    '币圈新人的几个致命错误',
    '持有BTC的第N天'
]

templates = [
    '{}，心态反而越来越好了。老韭菜都懂：\n\n1. 不要All In\n2. 不要玩合约\n3. 不要听小道消息\n4. 长期持有才是王道\n\n币圈不缺机会，缺的是耐心。',
    '{}，终于明白了一个道理：在币圈，活下来比赚快钱更重要。',
    '{}，分享一下我的仓位管理：\n\n现货：70%\nUSDT：20%\n山寨：10%\n\n永远不要让本金归零。',
    '{}，币圈最大的误区就是觉得自己能抄到底。真正的高手都是分批建仓。',
]

topic = random.choice(topics)
template = random.choice(templates)
content = template.format(topic)

# Post
r = requests.post('https://www.binance.com/bapi/communication/v1/submit/user/post',
    headers={'Content-Type': 'application/json', 'X-Mbx-Apikey': API_KEY},
    json={'content': content})

print('Status:', r.status_code)
if r.status_code == 200:
    data = r.json()
    if data.get('success'):
        print('Post ID:', data.get('data', {}).get('postId'))
    else:
        print('Error:', data)
else:
    print('Response:', r.text[:200])
