import re

with open('cmodel_emc_dashboard.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Section 4 HTML (Range)
html = html.replace(
    '<p style="font-size: 0.9em; line-height: 1.4; color: #475569;">现在，我们把这串 Bins 里的第一个 <code>1</code> (假设这是小概率事件 LPS) 喂进底层的算术引擎。我为你准备了两种体验方式：自动播放的全过程动画，或者你可以手动点击按钮一步步推演底层运算过程：</p>',
    '<p style="font-size: 0.9em; line-height: 1.4; color: #475569;">现在，我们把这串 Bins 里的第一个 <code>1</code> (假设这是小概率事件 LPS) 喂进底层的算术引擎。你可以手动点击按钮一步步推演底层运算过程，或者直接点击“自动推演”：</p>'
)

# Remove the GIF from Section 4
html = re.sub(r'<!-- Python Auto-play GIF -->.*?</div>\s*<!-- Interactive Manual Steps -->', '<!-- Interactive Manual Steps -->', html, flags=re.DOTALL)

# Add btn-tutor-auto
html = html.replace(
    '<button id="btn-tutor-next" style="background: var(--primary); color: white; border: none; padding: 8px 16px; border-radius: 6px; cursor: pointer; font-weight: bold;">执行下一步推演</button>',
    '<div style="display: flex; gap: 10px;"><button id="btn-tutor-next" style="background: var(--primary); color: white; border: none; padding: 8px 16px; border-radius: 6px; cursor: pointer; font-weight: bold;">执行下一步推演</button><button id="btn-tutor-auto" style="background: #3b82f6; color: white; border: none; padding: 8px 16px; border-radius: 6px; cursor: pointer; font-weight: bold;">自动推演</button></div>'
)

# 2. Add Section 4 JS (Range)
js_tutor_auto = """
        const btnTutorAuto = document.getElementById('btn-tutor-auto');
        let autoTutorInterval = null;
        
        btnTutorAuto.addEventListener('click', () => {
            if (autoTutorInterval) {
                clearInterval(autoTutorInterval);
                autoTutorInterval = null;
                btnTutorAuto.innerText = "自动推演";
                return;
            }
            btnTutorAuto.innerText = "停止推演";
            if (curTutorStep >= tutorSteps.length - 1) {
                btnTutorNext.click(); // Reset to start
            }
            autoTutorInterval = setInterval(() => {
                btnTutorNext.click();
                if (curTutorStep >= tutorSteps.length - 1 || curTutorStep === 0) {
                    clearInterval(autoTutorInterval);
                    autoTutorInterval = null;
                    btnTutorAuto.innerText = "自动推演";
                }
            }, 1500);
        });
"""
# Insert after lblHigh declaration
html = html.replace("const lblHigh = document.getElementById('tutor-label-high');", "const lblHigh = document.getElementById('tutor-label-high');\n" + js_tutor_auto)

# 3. Update Section 7 HTML (Coeff)
html = html.replace(
    '<p style="font-size: 0.9em; line-height: 1.6; color: #4c1d95;">\n            在扫描路线上，16 个系数并不是“读到一个就立刻把它编完”。相反，HEVC 会把这 16 个数据排成一列，然后<strong>对其进行 5 次独立检阅</strong>，每次只提取它们身上的一点特征！<br><br>\n            同样，我为你准备了两种体验方式：一种是 Python 生成的自动播放动画（一镜到底了解全貌），另一种是可以自己控制节奏的手动点击推演器。\n        </p>',
    '<p style="font-size: 0.9em; line-height: 1.6; color: #4c1d95;">\n            在扫描路线上，16 个系数并不是“读到一个就立刻把它编完”。相反，HEVC 会把这 16 个数据排成一列，然后<strong>对其进行 5 次独立检阅</strong>，每次只提取它们身上的一点特征！你可以点击“下一趟”手动推演，或者直接点击“自动扫描全景”：\n        </p>'
)

# Remove the GIF from Section 7
html = re.sub(r'<!-- Python Auto-play GIF -->.*?</div>\s*<!-- Animation Block -->', '<!-- Animation Block -->', html, flags=re.DOTALL)

# Add btnCoeffAuto
html = html.replace(
    '<button id="btnCoeffNext" style="background: #8b5cf6; color: #fff; border: none; padding: 8px 16px; border-radius: 6px; cursor: pointer; font-weight: bold; font-family: Inter, sans-serif; transition: 0.2s;">开始第 1 趟扫描</button>',
    '<div style="display: flex; gap: 10px;"><button id="btnCoeffNext" style="background: #8b5cf6; color: #fff; border: none; padding: 8px 16px; border-radius: 6px; cursor: pointer; font-weight: bold; font-family: Inter, sans-serif; transition: 0.2s;">开始第 1 趟扫描</button><button id="btnCoeffAuto" style="background: #a855f7; color: #fff; border: none; padding: 8px 16px; border-radius: 6px; cursor: pointer; font-weight: bold; font-family: Inter, sans-serif; transition: 0.2s;">自动扫描全景</button></div>'
)

# 4. Add Section 7 JS (Coeff)
js_coeff_auto = """
        const btnCoeffAuto = document.getElementById('btnCoeffAuto');
        let autoCoeffInterval = null;
        
        btnCoeffAuto.addEventListener('click', () => {
            if (autoCoeffInterval) {
                clearInterval(autoCoeffInterval);
                autoCoeffInterval = null;
                btnCoeffAuto.innerText = "自动扫描全景";
                return;
            }
            btnCoeffAuto.innerText = "停止扫描";
            if (passState >= 5) {
                btnCoeff.click(); // Reset to start
            }
            autoCoeffInterval = setInterval(() => {
                btnCoeff.click();
                if (passState >= 5 || passState === 0) {
                    clearInterval(autoCoeffInterval);
                    autoCoeffInterval = null;
                    btnCoeffAuto.innerText = "自动扫描全景";
                }
            }, 1500);
        });
"""
# Insert after coeff container declaration
html = html.replace("const coeffContainer = document.getElementById('coeffArrayContainer');", "const coeffContainer = document.getElementById('coeffArrayContainer');\n" + js_coeff_auto)

with open('cmodel_emc_dashboard.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("HTML Auto-play modification successful.")
