import subprocess
import os

os.chdir('seo')

# Add files
subprocess.run(['git', 'add', 'article/fashi-shengji-luxian.html'])
subprocess.run(['git', 'add', 'index.html'])

# Commit
result = subprocess.run(['git', 'commit', '-m', '新增文章：复古版本法师升级攻略'], capture_output=True, text=True)
print(result.stdout)
print(result.stderr)

# Push
result = subprocess.run(['git', 'push'], capture_output=True, text=True)
print(result.stdout)
print(result.stderr)
