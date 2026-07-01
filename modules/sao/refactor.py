import re

with open('cmodel_emc_dashboard.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Split by <h2> tags. We need to be careful with regex.
# Let's find the exact indices of each <h2
h2_matches = list(re.finditer(r'<h2.*?>', content))

def get_section(idx):
    start = h2_matches[idx].start()
    end = h2_matches[idx+1].start() if idx + 1 < len(h2_matches) else content.find('</div>\n</div>\n\n<script>')
    if end == -1: end = content.find('</div>\n</div>\n<script>')
    if end == -1: end = len(content)
    return content[start:end]

# Indices (0-indexed):
# 0: TOC (<h2 class="toc-title">目录导航</h2>)
# 1: Sec 1
# 2: Sec 2
# 3: Sec 3 (CABAC 编码全链路剖析)
# 4: Sec 4 (语法元素速查表)
# 5: Sec 5 (比特流没有分隔符)
# 6: Sec 6 (完美对称)
# 7: Sec 7 (16个残差系数)
# 8: Sec 8 (解码器怎么知道解完了)
# 9: Sec 9 (码表规则)

header = content[:h2_matches[0].start()]
toc_sec = get_section(0)
sec1 = get_section(1)
sec2 = get_section(2)
sec3 = get_section(3)
sec4 = get_section(4)
sec5 = get_section(5)
sec6 = get_section(6)
sec7 = get_section(7)
sec8 = get_section(8)
sec9 = get_section(9)

footer_start = h2_matches[9].start() + len(sec9)
footer = content[footer_start:]

# Banners
def get_banner(part_num, title, desc, color):
    return f"""
    <div style="background: linear-gradient(135deg, {color} 0%, #ffffff 100%); padding: 20px 30px; border-radius: 12px; margin-top: 50px; margin-bottom: 30px; border-left: 8px solid {color}; box-shadow: 0 4px 15px rgba(0,0,0,0.05);">
        <h1 style="margin: 0; color: #1e293b; font-size: 1.8em;">Part {part_num}: {title}</h1>
        <p style="margin: 10px 0 0 0; color: #475569; font-size: 0.95em;">{desc}</p>
    </div>
"""

part1_banner = get_banner('I', '宏观调度层 (System & Scheduling)', '解析 EMC 模块的系统定位与底层架构，以及空间树形状态机的运转机制。', '#3b82f6')
part2_banner = get_banner('II', '压缩引擎层 (CABAC Compression Engine)', '深入 CABAC 的心脏：从 CU 语法元素字典的映射，到最终算术压缩挤出比特的完整流程。', '#10b981')
part3_banner = get_banner('III', '黑科技解密与大一统架构 (Bitstream Decryption & Unified Architecture)', '揭秘 HEVC 最神奇的无分隔符解码技术，以及编解码架构的对称之美。', '#8b5cf6')
part4_banner = get_banner('IV', '终极实战 (Ultimate Practical)', '直面最复杂的场景：16 个残差系数的五趟独立扫描编码推演。', '#f59e0b')

# Rename sections using regex
def rename_h2(sec_html, new_title):
    return re.sub(r'<h2.*?>.*?</h2>', f'<h2 style="border-top: 2px solid #e2e8f0; padding-top: 30px; margin-top: 40px; color: var(--primary);">{new_title}</h2>', sec_html, count=1)

def demote_to_h3(sec_html, new_title, color='#db2777'):
    return re.sub(r'<h2.*?>.*?</h2>', f'<h3 style="margin-top: 40px; color: {color}; border-left: 4px solid {color}; padding-left: 10px;">{new_title}</h3>', sec_html, count=1)

# Modify sections
sec1 = rename_h2(sec1, '1. 宏观控制层：EMC 模块定位与异步 FIFO 架构')
sec2 = rename_h2(sec2, '2. 空间遍历：树形 FSM 状态机与 Quad-Tree')
sec4_renamed = rename_h2(sec4, '3. 字典与映射：CU 级语法元素速查表')
sec3_renamed = rename_h2(sec3, '4. 核心机制：CABAC 编码全链路剖析')
sec5 = rename_h2(sec5, '5. 深度解密：没有分隔符的比特流，解码端凭什么能看懂？')
sec5 = sec5.replace('<h2 style="border-top: 2px solid #e2e8f0; padding-top: 30px; margin-top: 40px; color: var(--primary);">5. 深度解密：没有分隔符的比特流，解码端凭什么能看懂？</h2>',
                    '<h2 style="border-top: 2px solid #e2e8f0; padding-top: 30px; margin-top: 40px; color: var(--primary);">5. 深度解密：没有分隔符的比特流，解码端凭什么能看懂？</h2>\n    <h3 style="margin-top: 30px; color: #4c1d95; border-left: 4px solid #4c1d95; padding-left: 10px;">5.1 宏观领航：FSM 状态机与协议默契</h3>')

sec8_h3 = demote_to_h3(sec8, '5.2 微观刹车：自终止的前缀码机制', '#db2777')
sec9_h3 = demote_to_h3(sec9, '5.3 底层兵法：HEVC 的四大核心二值化码表规则', '#b45309')

# Combine 5, 8, 9
sec5_combo = sec5 + '\n' + sec8_h3 + '\n' + sec9_h3

sec6_renamed = rename_h2(sec6, '6. 架构大一统：编解码的完美对称之美')
sec7_renamed = rename_h2(sec7, '7. 压轴实战：16 个残差系数 (Coeff) 的“五趟扫描”')

new_body = (
    part1_banner + sec1 + sec2 +
    part2_banner + sec4_renamed + sec3_renamed +
    part3_banner + sec5_combo + sec6_renamed +
    part4_banner + sec7_renamed
)

# Reassemble
new_content = header + toc_sec + new_body + footer

with open('cmodel_emc_dashboard.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Refactoring complete.")
