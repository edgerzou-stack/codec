import re

with open('cmodel_emc_dashboard.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Delete duplicate binarization text in Section 4.
# The block starts with <h4 style="margin-top: 0; color: #333; border-bottom: 2px solid #f1f5f9; padding-bottom: 10px;">🛠️ 深度解析：Binarizer (二值化器) 的三大核心兵器</h4>
# And ends before <div style="display: flex; gap: 20px; align-items: stretch;"> (which is the beginning of context modeling) or just before <!-- 算术编码与上下文模型推演区 -->

# Let's use regex to remove that specific h4 block.
dup_pattern = re.compile(r'<h4 style="margin-top: 0; color: #333; border-bottom: 2px solid #f1f5f9; padding-bottom: 10px;">🛠️ 深度解析：Binarizer \(二值化器\) 的三大核心兵器</h4>.*?</ul>\s*</div>\s*', re.DOTALL)
html = dup_pattern.sub('', html)

# 2. Extract Section 7 (Coeff)
sec7_pattern = re.compile(r'<h2 style="border-top: 2px solid #e2e8f0; padding-top: 30px; margin-top: 40px; color: var\(--primary\);">7\. 压轴实战：16 个残差系数 \(Coeff\) 的“五趟扫描”</h2>(.*?)</div>\s*</div>\s*<script>', re.DOTALL)
sec7_match = sec7_pattern.search(html)
if sec7_match:
    sec7_content = sec7_match.group(1)
    # Remove Section 7 and Part IV banner from the bottom
    html = sec7_pattern.sub('</div>\n</div>\n\n<script>', html)
    part4_banner_pattern = re.compile(r'<div style="background: linear-gradient\(135deg, #f59e0b 0%, #ffffff 100%\);.*?</div>', re.DOTALL)
    html = part4_banner_pattern.sub('', html)
    
    # Change Coeff header to 4.3 h3
    sec7_content = '<h3 style="margin-top: 40px; color: #8b5cf6; border-left: 4px solid #8b5cf6; padding-left: 10px;">4.3 压轴实战：16 个残差系数 (Coeff) 的“五趟扫描”</h3>\n' + sec7_content
    
    # Insert sec7_content at the end of Section 4 (before Part III banner)
    part3_banner_idx = html.find('<div style="background: linear-gradient(135deg, #8b5cf6')
    if part3_banner_idx != -1:
        html = html[:part3_banner_idx] + sec7_content + '\n' + html[part3_banner_idx:]

# 3. Extract Section 6 (Symmetry)
sec6_pattern = re.compile(r'<h2 style="border-top: 2px solid #e2e8f0; padding-top: 30px; margin-top: 40px; color: var\(--primary\);">6\. 架构大一统：编解码的完美对称之美</h2>(.*?)(?=<div style="background: linear-gradient|<script|</div>\s*</div>\s*<script)', re.DOTALL)
sec6_match = sec6_pattern.search(html)
if sec6_match:
    sec6_content = sec6_match.group(1)
    html = sec6_pattern.sub('', html)
    
    # Change Symmetry header to 5.4 h3
    sec6_content = '<h3 style="margin-top: 40px; color: var(--primary); border-left: 4px solid var(--primary); padding-left: 10px;">5.4 架构大一统：编解码的完美对称之美</h3>\n' + sec6_content
    
    # Insert sec6_content at the end of Section 5
    # Since Section 6 was originally after Section 5, it might just need to be appended before the end of the container.
    # But wait, we just removed Sec 6, so we can insert it right before <script> or wherever Section 5 ends.
    # Section 5 is now the last section in the DOM!
    end_idx = html.find('</div>\n</div>\n\n<script>')
    if end_idx == -1: end_idx = html.find('</div>\n</div>\n<script>')
    if end_idx != -1:
        html = html[:end_idx] + sec6_content + '\n' + html[end_idx:]

# 4. Add 4.1 and 4.2 headers
# Find "第一步：语法元素 -> Bins (二值化)" and change context to 4.1
html = html.replace(
    '<div style="flex: 1; background: #fff0f2; border: 1px dashed #f43f5e; padding: 15px; border-radius: 8px;">',
    '<h3 style="margin-top: 30px; margin-bottom: 20px; color: #0284c7; border-left: 4px solid #0284c7; padding-left: 10px;">4.1 算术编码的微观推演 (MVD=1 示例)</h3>\n                <div style="flex: 1; background: #fff0f2; border: 1px dashed #f43f5e; padding: 15px; border-radius: 8px;">'
)

# Find "深入灵魂的拷问" and change it to 4.2
html = html.replace(
    '<p style="font-size: 0.85em; margin: 0; color: #0c4a6e; line-height: 1.5;">\n                        <strong>🔥 深入灵魂的拷问：Range 怎么按概率切分？需要算乘法吗？</strong><br>',
    '</p><h3 style="margin-top: 30px; margin-bottom: 15px; color: #0369a1; border-left: 4px solid #0369a1; padding-left: 10px;">4.2 乘法器的终结：Range 查表切分机制</h3>\n<p style="font-size: 0.85em; margin: 0; color: #0c4a6e; line-height: 1.5;">\n                        <strong>🔥 深入灵魂的拷问：Range 怎么按概率切分？需要算乘法吗？</strong><br>'
)

with open('cmodel_emc_dashboard.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Final HTML refactoring complete.")
