import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches

matplotlib.rcParams['font.sans-serif'] = ['PingFang SC', 'Heiti TC', 'Arial Unicode MS', 'sans-serif']
matplotlib.rcParams['axes.unicode_minus'] = False

fig, ax = plt.subplots(figsize=(10, 4), dpi=120)
ax.set_xlim(-0.5, 7.5)
ax.set_ylim(0, 5)
ax.axis('off')

coeffs = [0, 0, 1, 1, -2, 4, 15]
boxes = []
texts_val = []
texts_flag = []

for i, val in enumerate(coeffs):
    box = patches.Rectangle((i+0.1, 1), 0.8, 1.5, facecolor='#f8fafc', edgecolor='#cbd5e1', lw=2, zorder=1)
    ax.add_patch(box)
    boxes.append(box)
    tv = ax.text(i+0.5, 1.9, str(val), color='#1e293b', weight='bold', ha='center', va='center', fontsize=16)
    texts_val.append(tv)
    tf = ax.text(i+0.5, 1.3, '', color='#94a3b8', weight='bold', ha='center', va='center', fontsize=12)
    texts_flag.append(tf)

title = ax.text(3.5, 4, 'Step 0: Initial Array', color='#1e293b', weight='bold', ha='center', va='center', fontsize=16)
desc = ax.text(3.5, 3.2, 'Ready for 5-pass scanning', color='#475569', ha='center', va='center', fontsize=13)

def reset_style():
    for b in boxes:
        b.set_facecolor('#f8fafc')
        b.set_edgecolor('#cbd5e1')
    for tf in texts_flag:
        tf.set_text('')

def update(frame):
    if frame < 15: # Initial
        reset_style()
        title.set_text('初始状态 (Initial)')
        desc.set_text('扫描获得的一维残差系数数组')
    elif frame < 35: # Pass 1
        reset_style()
        title.set_text('第 1 趟：sig_coeff_flag')
        desc.set_text('提取所有元素的非零标志 (0或1)')
        for i, val in enumerate(coeffs):
            boxes[i].set_facecolor('#d1fae5')
            boxes[i].set_edgecolor('#059669')
            texts_flag[i].set_text('sig=1' if val != 0 else 'sig=0')
            texts_flag[i].set_color('#059669')
    elif frame < 55: # Pass 2
        reset_style()
        title.set_text('第 2 趟：gt1_flag')
        desc.set_text('仅对非0元素，提取绝对值是否 > 1')
        for i, val in enumerate(coeffs):
            if val != 0:
                boxes[i].set_facecolor('#dbeafe')
                boxes[i].set_edgecolor('#2563eb')
                texts_flag[i].set_text('gt1=1' if abs(val) > 1 else 'gt1=0')
                texts_flag[i].set_color('#2563eb')
    elif frame < 75: # Pass 3
        reset_style()
        title.set_text('第 3 趟：gt2_flag')
        desc.set_text('仅对>1元素，提取绝对值是否 > 2')
        for i, val in enumerate(coeffs):
            if abs(val) > 1:
                boxes[i].set_facecolor('#f3e8ff')
                boxes[i].set_edgecolor('#9333ea')
                texts_flag[i].set_text('gt2=1' if abs(val) > 2 else 'gt2=0')
                texts_flag[i].set_color('#9333ea')
    elif frame < 95: # Pass 4
        reset_style()
        title.set_text('第 4 趟：sign_flag')
        desc.set_text('仅对非0元素，提取正负号 (走 Bypass 模式)')
        for i, val in enumerate(coeffs):
            if val != 0:
                boxes[i].set_facecolor('#ffedd5')
                boxes[i].set_edgecolor('#ea580c')
                texts_flag[i].set_text('sign=+' if val > 0 else 'sign=-')
                texts_flag[i].set_color('#ea580c')
    elif frame < 125: # Pass 5
        reset_style()
        title.set_text('第 5 趟：coeff_abs_level_remaining')
        desc.set_text('提取剩余巨大数值 (TR+EGk Bypass 模式)')
        for i, val in enumerate(coeffs):
            if abs(val) > 2:
                rem = abs(val) - 3
                boxes[i].set_facecolor('#ffe4e6')
                boxes[i].set_edgecolor('#e11d48')
                texts_flag[i].set_text(f'rem={rem}')
                texts_flag[i].set_color('#e11d48')
    return boxes + texts_flag + [title, desc]

ani = animation.FuncAnimation(fig, update, frames=140, interval=100, blit=True)
ani.save('cabac_coeff_anim.gif', writer='pillow', fps=10)
print("GIF generated successfully")
