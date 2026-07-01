import re

with open('cmodel_emc_dashboard.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Fix the unclosed div at the end of the Coeff section (before Chapter 4)
html = html.replace(
    '        </div>\n        \n<h2 style="border-top: 2px solid #e2e8f0; padding-top: 30px; margin-top: 40px; color: var(--primary);">4. 深度解密',
    '        </div>\n    </div>\n        \n<h2 style="border-top: 2px solid #e2e8f0; padding-top: 30px; margin-top: 40px; color: var(--primary);">4. 深度解密'
)

# 2. Change the 4 binarization cards to be exactly 2x2
html = html.replace(
    'grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; margin-bottom: 30px;',
    'grid-template-columns: repeat(2, 1fr); gap: 20px; margin-bottom: 30px;'
)

with open('cmodel_emc_dashboard.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Layouts fixed successfully.")
