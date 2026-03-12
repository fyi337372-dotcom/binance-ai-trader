# -*- coding: utf-8 -*-
with open('seo/index.html', 'rb') as f:
    c = f.read()

# Fix the pattern
old = b'jiqiao.html">\xe4\xbc\xa0\xe5\xa5\x87\xe6\x8a\x80?\x3e/a>'
new = b'jiqiao.html">\xe4\xbc\xa0\xe5\xa5\x87\xe6\x8a\x80\xe5\xb7\xa7</a>'

c = c.replace(old, new)

# Also fix xinwen if needed
old2 = b'xinwen.html">\xe6\xb8\xb8\xe6\x88\x8f\xe8\xb5\x84\xe8\xae\xaf?\x3e/a>'
new2 = b'xinwen.html">\xe6\xb8\xb8\xe6\x88\x8f\xe8\xb5\x84\xe8\xae\xaf</a>'

c = c.replace(old2, new2)

with open('seo/index.html', 'wb') as f:
    f.write(c)

print('Done!')
