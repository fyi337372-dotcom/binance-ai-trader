# -*- coding: utf-8 -*-
with open('seo/index.html', 'rb') as f:
    content = f.read()

# Find and fix the corrupted description ending
# Look for: ...成长??> 
corrupted = b'\xe9\x95\xbf??\x3e'  # 成长??>
correct = b'\xe9\x95\xbf\">'  # 成长">

if corrupted in content:
    content = content.replace(corrupted, correct)
    print("Fixed description ending")

# Fix keywords: 技巧?> should be 技巧">
corrupted2 = b'\xe6\x8a\x80?\xe7\x83\xad'  # 技巧?>
correct2 = b'\xe6\x8a\x80\xe5\xb7\xa7\xe7\x83\xad'  # 技巧">

if corrupted2 in content:
    content = content.replace(corrupted2, correct2)
    print("Fixed keywords")

# More fixes for patterns like ��?
# Let's check all occurrences of single ? followed by >
content_str = content.decode('utf-8', errors='ignore')

# Fix navigation jiqiao.html
content_str = content_str.replace('jiqiao.html">游戏技�', 'jiqiao.html">游戏技巧')
content_str = content_str.replace('�', '')

# Fix buttons
content_str = content_str.replace('�', '')

with open('seo/index.html', 'w', encoding='utf-8') as f:
    f.write(content_str)

print("All fixes applied!")
