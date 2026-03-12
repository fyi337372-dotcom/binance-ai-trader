# -*- coding: utf-8 -*-
with open('seo/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add new article before the last </div></section>
old_pattern = '''                    <a href="article/caijue-zhang.html" class="btn">阅读全文 →</a>
                </div>
            </div>

        </div>

    </section>
    
    
    <section class="tips-section">'''

new_pattern = '''                    <a href="article/caijue-zhang.html" class="btn">阅读全文 →</a>
                </div>
                
                <div class="article-card">
                    <span class="category">打宝攻略</span>
                    <h3>传奇sf祖玛寺庙怎么打？老玩家分享祖玛七层跑图和装备掉落</h3>
                    <p>传奇sf祖玛寺庙攻略，老玩家分享祖玛七层跑图路线</p>
                    <div class="meta">更新时间：2026-03-05</div>
                    <a href="article/zuma-simi.html" class="btn">阅读全文 →</a>
                </div>
            </div>

        </div>

    </section>
    
    
    <section class="tips-section">'''

content = content.replace(old_pattern, new_pattern)

with open('seo/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

# Also add to jiqiao.html
with open('seo/jiqiao.html', 'r', encoding='utf-8') as f:
    jiqiao_content = f.read()

jiqiao_old = '''                    <a href="article/caijue-zhang.html" class="btn">阅读全文 →</a>
                </div>
                
            </div>
        </div>
    </section>
    
    <footer>'''

jiqiao_new = '''                    <a href="article/caijue-zhang.html" class="btn">阅读全文 →</a>
                </div>
                
                <div class="article-card">
                    <span class="category">打宝攻略</span>
                    <h3>传奇sf祖玛寺庙怎么打？老玩家分享祖玛七层跑图和装备掉落</h3>
                    <p>传奇sf祖玛寺庙攻略，老玩家分享祖玛七层跑图路线</p>
                    <div class="meta">更新时间：2026-03-05</div>
                    <a href="article/zuma-simi.html" class="btn">阅读全文 →</a>
                </div>
                
            </div>
        </div>
    </section>
    
    <footer>'''

jiqiao_content = jiqiao_content.replace(jiqiao_old, jiqiao_new)

with open('seo/jiqiao.html', 'w', encoding='utf-8') as f:
    f.write(jiqiao_content)

print("Done!")
