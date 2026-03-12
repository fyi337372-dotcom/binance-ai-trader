# -*- coding: utf-8 -*-
import re

with open('seo/index.html', 'rb') as f:
    c = f.read()

# Fix: 传奇技?/a> -> 传奇技巧</a>
c = re.sub(b'>\xe4\xbc\xa0\xe5\xa5\x87\xe6\x8a\x80\?</a>>', b'>\xe4\xbc\xa0\xe5\xa5\x87\xe6\x8a\x80\xe5\xb7\xa7</a>', c)

# Or try simpler: replace any ? between Chinese chars and /a>
c = re.sub(b'技\?</a>>', b'巧</a>', c)

with open('seo/index.html', 'wb') as f:
    f.write(c)

print('Done!')
