import re

with open('cmodel_emc_dashboard.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Remove the broken 3.5 block from inside the 3.4 box.
broken_35_pattern = re.compile(r'\s*<hr style="border: none; border-top: 1px dashed #bae6fd; margin: 10px 0;">\s*</p><h3>3\.5 乘法器的终结：Range 查表切分机制</h3>\s*<p style="font-size: 0\.85em; margin: 0; color: #0c4a6e; line-height: 1\.5;">\s*<strong>🔥 深入灵魂的拷问：Range 怎么按概率切分？需要算乘法吗？</strong><br>\s*你可能会想：切分区间不就是 <code>R_LPS = Range × P_LPS</code> 吗？在芯片里算乘法可是非常昂贵且缓慢的！<br>\s*HEVC/H\.264 的 CABAC 最伟大的发明之一就是<strong>“无乘法区间划分” \(Multiplication-free\)</strong>。它直接用查表 \(LUT\) 替代了乘法：<br>\s*因为归一化机制的存在，<code>Range</code> 永远被卡在 <strong>\[256, 510\]</strong> 之间（最高位恒定为 1）。引擎只需提取 Range 的第 6、7 位作为“区间近似索引 \(0~3\)”，再结合当前上下文的“概率状态索引 pStateIdx \(0~63\)”，去查一张硬编码的 <strong>64x4 二维常量数组 \(RangeTabLps\)</strong>。<br>\s*一瞬间，查表得出 <code>R_LPS</code>。然后加法器一跑：<code>R_MPS = Range - R_LPS</code>。整个切分过程 0 乘法、纯组合逻辑，这也是 CABAC 算盘能跑出超高吞吐率的底层根基！\s*</p>', re.DOTALL)

html = broken_35_pattern.sub('', html)

# 2. Insert the correctly formatted 3.5 block before the <script> tag.
new_35_block = """
    <div style="background: #ffffff; padding: 25px; border-radius: 12px; border: 1px solid #e2e8f0; margin-bottom: 30px; box-shadow: 0 4px 10px rgba(0,0,0,0.03);">
        <h3>3.5 乘法器的终结：Range 查表切分机制</h3>
        <div style="background: #e0f2fe; padding: 15px; border-radius: 8px; border-left: 4px solid #0284c7; margin-top: 15px;">
            <p style="font-size: 0.95em; margin: 0; color: #0c4a6e; line-height: 1.6;">
                <strong>🔥 深入灵魂的拷问：Range 怎么按概率切分？需要算乘法吗？</strong><br><br>
                你可能会想：切分区间不就是 <code>R_LPS = Range × P_LPS</code> 吗？在芯片里算乘法可是非常昂贵且缓慢的！<br><br>
                HEVC/H.264 的 CABAC 最伟大的发明之一就是<strong>“无乘法区间划分” (Multiplication-free)</strong>。它直接用查表 (LUT) 替代了乘法：<br><br>
                因为归一化机制的存在，<code>Range</code> 永远被卡在 <strong>[256, 510]</strong> 之间（最高位恒定为 1）。引擎只需提取 Range 的第 6、7 位作为“区间近似索引 (0~3)”，再结合当前上下文的“概率状态索引 pStateIdx (0~63)”，去查一张硬编码的 <strong>64x4 二维常量数组 (RangeTabLps)</strong>。<br><br>
                一瞬间，查表得出 <code>R_LPS</code>。然后加法器一跑：<code>R_MPS = Range - R_LPS</code>。整个切分过程 0 乘法、纯组合逻辑，这也是 CABAC 算盘能跑出超高吞吐率的底层根基！
            </p>
        </div>
    </div>
"""

# Find the start of the script tag that follows the 3.4 box.
script_idx = html.find('<script>\n        const tutorSteps = [')
if script_idx != -1:
    html = html[:script_idx] + new_35_block + html[script_idx:]

with open('cmodel_emc_dashboard.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Layout fixed successfully.")
