# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('seo/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Check for replacement characters
if '\ufffd' in content:
    print("Found replacement characters - file is corrupted")
    # Count them
    count = content.count('\ufffd')
    print(f"Found {count} replacement characters")
else:
    print("No replacement characters found")

# Let's check the title line specifically
lines = content.split('\n')
for i, line in enumerate(lines[:10], 1):
    if '<title>' in line:
        print(f"Title line {i}: {line}")
    if 'description' in line:
        print(f"Meta desc line {i}: {line[:120]}")
