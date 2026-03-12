# -*- coding: utf-8 -*-
import re

with open('seo/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    c = f.read()

# Fix using regex - find pattern like 技?/a> and replace
c = re.sub(r'技\?</a>', '巧</a>', c)

with open('seo/index.html', 'w', encoding='utf-8') as f:
    f.write(c)

print('Done!')
