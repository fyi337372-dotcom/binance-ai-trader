# -*- coding: utf-8 -*-
import os
import re
from datetime import datetime

# Get all article files
articles = []
for f in os.listdir('seo/article'):
    if f.endswith('.html'):
        path = f'seo/article/{f}'
        # Extract title from the file
        with open(path, 'r', encoding='utf-8', errors='ignore') as fp:
            content = fp.read()
            match = re.search(r'<title>(.*?)</title>', content)
            title = match.group(1) if match else f.replace('.html', '')
            
            # Extract date
            date_match = re.search(r'(\d{4})-(\d{2})-(\d{2})', content)
            date = date_match.group(0) if date_match else '2026-03-04'
            
            # Extract category
            cat_match = re.search(r'<span class="category">(.*?)</span>', content)
            category = cat_match.group(1) if cat_match else '游戏攻略'
            
            articles.append({
                'file': f,
                'title': title,
                'date': date,
                'category': category
            })

# Sort by date descending
articles.sort(key=lambda x: x['date'], reverse=True)

# Take latest 30
latest = articles[:30]

for a in latest:
    print(f"{a['date']} {a['category']} {a['title']} -> {a['file']}")
