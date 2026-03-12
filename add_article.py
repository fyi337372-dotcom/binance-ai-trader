# -*- coding: utf-8 -*-
with open('seo/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the pattern and add new article
old_pattern = '''                    <a href="article/bairimen-ditu.html" class="btn">阅读全文 ?</a>

                </div>

            </div>

        </div>

    </section>
    
    
    <section class="tips-section">'''

new_pattern = '''                    <a href="article/bairimen-ditu.html" class="btn">阅读全文 →</a>

                </div>
                
                <div class="article-card">
                    <span class="category">武器攻略</span>
                    <h3>传奇sf裁决之杖怎么获得？老玩家分享裁决武器获取攻略和属性介绍</h3>
                    <p>传奇sf裁决之杖获取攻略，老玩家分享裁决武器属性</p>
                    <div class="meta">更新时间：2026-03-05</div>
                    <a href="article/caijue-zhang.html" class="btn">阅读全文 →</a>
                </div>
            </div>

        </div>

    </section>
    
    
    <section class="tips-section">'''

content = content.replace(old_pattern, new_pattern)

# Also fix remaining garbled chars in tips section
content = content.replace('实用技?/h2>', '实用技巧</h2>')
content = content.replace('快捷键使?/h4>', '快捷键使用</h4>')
content = content.replace('好东?/p>', '好东西</p>')
content = content.replace('方?/p>', '方法</p>')

with open('seo/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done!")
