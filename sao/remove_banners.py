import re

with open('cmodel_emc_dashboard.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Delete Part banners
banner_pattern = re.compile(r'<div style="background: linear-gradient\(135deg.*?</p>\s*</div>\s*', re.DOTALL)
html = banner_pattern.sub('', html)

with open('cmodel_emc_dashboard.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Removed all Part banners successfully.")
