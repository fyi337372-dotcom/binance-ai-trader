# -*- coding: utf-8 -*-
with open('seo/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old = '''                    <a href="article/chiyue-xiagu.html" class="btn">阅读全文 →</a>
                </div>
            </div>

        </div>

    </section>
    
    
    <section class="tips-section">'''

new = '''                    <a href="article/chiyue-xiagu.html" class="btn">阅读全文 →</a>
                </div>
                
                <div class="article-card">
                    <span class="category">打宝攻略</span>
                    <h3>传奇sf魔龙血域怎么打？老玩家分享魔龙岭走法和魔龙教主攻略</h3>
                    <p>传奇sf魔龙血域攻略，老玩家分享魔龙岭走法</p>
                    <div class="meta">更新时间：2026-03-05</div>
                    <a href="article/molong-xueyu.html" class="btn">阅读全文 →</a>
                </div>
            </div>

        </div>

    </section>
    
    
    <section class="tips-section">'''

content = content.replace(old, new)

with open('seo/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

# Add to jiqiao.html
with open('seo/jiqiao.html', 'r', encoding='utf-8') as f:
    jiqiao = f.read()

old2 = '''                    <a href="article/chiyue-xiagu.html" class="btn">阅读全文 →</a>
                </div>
                
            </div>
        </div>
    </section>
    
    <footer>'''

new2 = '''                    <a href="article/chiyue-xiagu.html" class="btn">阅读全文 →</a>
                </div>
                
                <div class="article-card">
                    <span class="category">打宝攻略</span>
                    <h3>传奇sf魔龙血域怎么打？老玩家分享魔龙岭走法和魔龙教主攻略</h3>
                    <p>传奇sf魔龙血域攻略，老玩家分享魔龙岭走法</p>
                    <div class="meta">更新时间：2026-03-05</div>
                    <a href="article/molong-xueyu.html" class="btn">阅读全文 →</a>
                </div>
                
            </div>
        </div>
    </section>
    
    <footer>'''

jiqiao = jiqiao.replace(old2, new2)

with open('seo/jiqiao.html', 'w', encoding='utf-8') as f:
    f.write(jiqiao)

print("Done!")
