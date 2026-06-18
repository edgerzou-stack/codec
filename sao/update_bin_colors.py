import re

with open('cmodel_emc_dashboard.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add IDs to the 4 cards in Section 3.2
html = html.replace(
    '<div style="background: #fff; padding: 20px; border-radius: 8px; border: 1px solid #e2e8f0; border-top: 4px solid #3b82f6; box-shadow: 0 2px 5px rgba(0,0,0,0.02);">\n            <h4 style="margin-top: 0; color: #1e3a8a;">1. 定长码 (Fixed Length, FL)</h4>',
    '<div id="bina-fl" style="background: #fff; padding: 20px; border-radius: 8px; border: 1px solid #e2e8f0; border-top: 4px solid #3b82f6; box-shadow: 0 2px 5px rgba(0,0,0,0.02);">\n            <h4 style="margin-top: 0; color: #1e3a8a;">1. 定长码 (Fixed Length, FL)</h4>'
)

html = html.replace(
    '<div style="background: #fff; padding: 20px; border-radius: 8px; border: 1px solid #e2e8f0; border-top: 4px solid #10b981; box-shadow: 0 2px 5px rgba(0,0,0,0.02);">\n            <h4 style="margin-top: 0; color: #064e3b;">2. 截断一元码 (Truncated Unary, TU)</h4>',
    '<div id="bina-tu" style="background: #fff; padding: 20px; border-radius: 8px; border: 1px solid #e2e8f0; border-top: 4px solid #10b981; box-shadow: 0 2px 5px rgba(0,0,0,0.02);">\n            <h4 style="margin-top: 0; color: #064e3b;">2. 截断一元码 (Truncated Unary, TU)</h4>'
)

html = html.replace(
    '<div style="background: #fff; padding: 20px; border-radius: 8px; border: 1px solid #e2e8f0; border-top: 4px solid #db2777; box-shadow: 0 2px 5px rgba(0,0,0,0.02);">\n            <h4 style="margin-top: 0; color: #831843;">3. 指数哥伦布 (Exp-Golomb, EGk)</h4>',
    '<div id="bina-egk" style="background: #fff; padding: 20px; border-radius: 8px; border: 1px solid #e2e8f0; border-top: 4px solid #db2777; box-shadow: 0 2px 5px rgba(0,0,0,0.02);">\n            <h4 style="margin-top: 0; color: #831843;">3. 指数哥伦布 (Exp-Golomb, EGk)</h4>'
)

html = html.replace(
    '<div style="background: #fff; padding: 20px; border-radius: 8px; border: 1px solid #e2e8f0; border-top: 4px solid #f59e0b; box-shadow: 0 2px 5px rgba(0,0,0,0.02);">\n            <h4 style="margin-top: 0; color: #78350f;">4. 截断莱斯 (Truncated Rice, TR)</h4>',
    '<div id="bina-tr" style="background: #fff; padding: 20px; border-radius: 8px; border: 1px solid #e2e8f0; border-top: 4px solid #f59e0b; box-shadow: 0 2px 5px rgba(0,0,0,0.02);">\n            <h4 style="margin-top: 0; color: #78350f;">4. 截断莱斯 (Truncated Rice, TR)</h4>'
)

# 2. Update the table cells to use matching colors and anchor links.
# Table FL
html = html.replace(
    '<td style="padding: 15px; color: #0284c7;">固定长度 (FL)</td>',
    '<td style="padding: 15px;"><a href="#bina-fl" style="color: #3b82f6; text-decoration: none; font-weight: bold; border-bottom: 1px dashed #3b82f6;">固定长度 (FL)</a></td>'
)

# Table Unary/TU
html = html.replace(
    '<td style="padding: 15px; color: #0284c7;">一元码 (Unary) 等</td>',
    '<td style="padding: 15px;"><a href="#bina-tu" style="color: #10b981; text-decoration: none; font-weight: bold; border-bottom: 1px dashed #10b981;">一元码 (Unary) 等</a></td>'
)

# Table EGk
html = html.replace(
    '<td style="padding: 15px; color: #d97706;">k阶指数哥伦布 (EGk)</td>',
    '<td style="padding: 15px;"><a href="#bina-egk" style="color: #db2777; text-decoration: none; font-weight: bold; border-bottom: 1px dashed #db2777;">k阶指数哥伦布 (EGk)</a></td>'
)

# Table TR
html = html.replace(
    '<td style="padding: 15px; color: #c026d3;">截断莱斯 (TR) + EGk</td>',
    '<td style="padding: 15px;"><a href="#bina-tr" style="color: #f59e0b; text-decoration: none; font-weight: bold; border-bottom: 1px dashed #f59e0b;">截断莱斯 (TR) + EGk</a></td>'
)

with open('cmodel_emc_dashboard.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Colors aligned and anchor links added successfully.")
