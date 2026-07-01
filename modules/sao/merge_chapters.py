import re

with open('cmodel_emc_dashboard.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Remove the duplicate binarization block.
# Let's extract the exact string from the file or use a very safe regex
dup_block_pattern = re.compile(
    r'<div style="background: #ffffff; padding: 25px; border-radius: 12px; border: 1px solid #e2e8f0; margin-bottom: 30px; box-shadow: 0 4px 10px rgba\(0,0,0,0\.03\);">\s*<h4 style="margin-top: 0; color: #333; border-bottom: 2px solid #f1f5f9; padding-bottom: 10px;">🛠️ 深度解析：Binarizer \(二值化器\) 的三大核心兵器</h4>.*?</div>\s*</div>\s*</div>', 
    re.DOTALL
)
html = dup_block_pattern.sub('', html)


# 2. Rename headers for Mega-Chapter 3
html = html.replace(
    '<h2 style="border-top: 2px solid #e2e8f0; padding-top: 30px; margin-top: 40px; color: var(--primary);">3. 字典与映射：CU 级语法元素速查表</h2>',
    '<h2 style="border-top: 2px solid #e2e8f0; padding-top: 30px; margin-top: 40px; color: var(--primary);">3. 核心机制：CABAC 语法字典与全链路剖析</h2>\n<h3 style="margin-top: 30px; color: #0284c7; border-left: 4px solid #0284c7; padding-left: 10px;">3.1 字典与映射：CU 级语法元素速查表</h3>'
)

html = html.replace(
    '<h2 style="border-top: 2px solid #e2e8f0; padding-top: 30px; margin-top: 40px; color: var(--primary);">4. 核心机制：CABAC 编码全链路剖析</h2>',
    '<h3 style="margin-top: 40px; color: #0284c7; border-left: 4px solid #0284c7; padding-left: 10px;">3.2 算术编码架构：CABAC 的完整数据流向</h3>'
)

# Remember that the "4.1" addition failed in the last script. I need to add 3.3 for the interactive block.
html = html.replace(
    '<div style="flex: 1; background: #fff0f2; border: 1px dashed #f43f5e; padding: 15px; border-radius: 8px;">',
    '<h3 style="margin-top: 30px; margin-bottom: 20px; color: #0284c7; border-left: 4px solid #0284c7; padding-left: 10px;">3.3 算术编码的微观推演 (MVD=1 示例)</h3>\n                <div style="flex: 1; background: #fff0f2; border: 1px dashed #f43f5e; padding: 15px; border-radius: 8px;">'
)

html = html.replace(
    '<h3 style="margin-top: 30px; margin-bottom: 15px; color: #0369a1; border-left: 4px solid #0369a1; padding-left: 10px;">4.2 乘法器的终结：Range 查表切分机制</h3>',
    '<h3 style="margin-top: 30px; margin-bottom: 15px; color: #0369a1; border-left: 4px solid #0369a1; padding-left: 10px;">3.4 乘法器的终结：Range 查表切分机制</h3>'
)

html = html.replace(
    '<h3 style="margin-top: 40px; color: #8b5cf6; border-left: 4px solid #8b5cf6; padding-left: 10px;">4.3 压轴实战：16 个残差系数 (Coeff) 的“五趟扫描”</h3>',
    '<h3 style="margin-top: 40px; color: #8b5cf6; border-left: 4px solid #8b5cf6; padding-left: 10px;">3.5 压轴实战：16 个残差系数 (Coeff) 的“五趟扫描”</h3>'
)

# 3. Rename headers for Mega-Chapter 4 (formerly 5)
html = html.replace(
    '<h2 style="border-top: 2px solid #e2e8f0; padding-top: 30px; margin-top: 40px; color: var(--primary);">5. 深度解密：没有分隔符的比特流，解码端凭什么能看懂？</h2>',
    '<h2 style="border-top: 2px solid #e2e8f0; padding-top: 30px; margin-top: 40px; color: var(--primary);">4. 深度解密：没有分隔符的比特流，解码端凭什么能看懂？</h2>'
)

html = html.replace(
    '<h3 style="margin-top: 30px; color: #4c1d95; border-left: 4px solid #4c1d95; padding-left: 10px;">5.1 宏观领航：FSM 状态机与协议默契</h3>',
    '<h3 style="margin-top: 30px; color: #4c1d95; border-left: 4px solid #4c1d95; padding-left: 10px;">4.1 宏观领航：FSM 状态机与协议默契</h3>'
)

html = html.replace(
    '<h3 style="margin-top: 40px; color: #db2777; border-left: 4px solid #db2777; padding-left: 10px;">5.2 微观刹车：自终止的前缀码机制</h3>',
    '<h3 style="margin-top: 40px; color: #db2777; border-left: 4px solid #db2777; padding-left: 10px;">4.2 微观刹车：自终止的前缀码机制</h3>'
)

html = html.replace(
    '<h3 style="margin-top: 40px; color: #b45309; border-left: 4px solid #b45309; padding-left: 10px;">5.3 底层兵法：HEVC 的四大核心二值化码表规则</h3>',
    '<h3 style="margin-top: 40px; color: #b45309; border-left: 4px solid #b45309; padding-left: 10px;">4.3 底层兵法：HEVC 的四大核心二值化码表规则</h3>'
)

html = html.replace(
    '<h3 style="margin-top: 40px; color: var(--primary); border-left: 4px solid var(--primary); padding-left: 10px;">5.4 架构大一统：编解码的完美对称之美</h3>',
    '<h3 style="margin-top: 40px; color: var(--primary); border-left: 4px solid var(--primary); padding-left: 10px;">4.4 架构大一统：编解码的完美对称之美</h3>'
)

with open('cmodel_emc_dashboard.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Merged Chapter 3 and 4 successfully.")
