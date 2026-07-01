import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches

# Try to set Mac Chinese fonts
matplotlib.rcParams['font.sans-serif'] = ['PingFang SC', 'Heiti TC', 'Arial Unicode MS', 'sans-serif']
matplotlib.rcParams['axes.unicode_minus'] = False

fig, ax = plt.subplots(figsize=(9, 4), dpi=120)
ax.set_xlim(-50, 550)
ax.set_ylim(-1, 4)
ax.axis('off')

# Background axis line
ax.plot([0, 500], [1, 1], color='#cbd5e1', lw=2, zorder=0)
ax.text(0, 0.7, '0', color='#94a3b8', ha='center', va='top', fontsize=10)
ax.text(500, 0.7, '500', color='#94a3b8', ha='center', va='top', fontsize=10)

bar = patches.Rectangle((0, 1), 500, 1, facecolor='#0284c7', edgecolor='#0369a1', lw=2, zorder=1)
ax.add_patch(bar)

text_range = ax.text(250, 1.5, 'Range = 500', color='white', weight='bold', ha='center', va='center', fontsize=12, zorder=2)
text_low = ax.text(0, 2.2, 'Low = 0', color='#0f172a', weight='bold', ha='center', va='bottom', fontsize=11)

text_title = ax.text(250, 3.5, 'Step 0: Initial State', color='#1e293b', weight='bold', ha='center', va='center', fontsize=15)
text_desc = ax.text(250, -0.5, 'Ready to encode first Bin=1 (LPS)', color='#475569', ha='center', va='center', fontsize=12)

def update(frame):
    if frame < 20: # 0-1s: Initial
        bar.set_x(0)
        bar.set_width(500)
        bar.set_facecolor('#0284c7')
        text_range.set_text('Range = 500')
        text_range.set_position((250, 1.5))
        text_low.set_text('Low = 0')
        text_low.set_position((0, 2.2))
        text_title.set_text('初始状态 (Initial)')
        text_desc.set_text('准备编码 Bin=1。当前 Range=500, Low=0')
    elif frame < 50: # 1-2.5s: Split MPS/LPS
        bar.set_facecolor('#0ea5e9')
        text_range.set_text('MPS (400) | LPS (100)')
        text_title.set_text('第一步：切分概率空间 (Split)')
        text_desc.set_text('假设概率模型预测 p(LPS)=20%。\nR_LPS = 500*20%=100, R_MPS = 400')
    elif frame < 80: # 2.5-4s: Jump
        progress = (frame - 50) / 30.0
        # Easing function (smoothstep)
        progress = progress * progress * (3 - 2 * progress)
        cur_x = 0 + 400 * progress
        cur_w = 500 - 400 * progress
        bar.set_x(cur_x)
        bar.set_width(cur_w)
        bar.set_facecolor('#f59e0b')
        text_range.set_text('Range=100')
        text_range.set_position((cur_x + cur_w/2, 1.5))
        text_low.set_text(f'Low={int(cur_x)}')
        text_low.set_position((cur_x, 2.2))
        text_title.set_text('第二步：区间跳跃 (Encode LPS)')
        text_desc.set_text('由于输入是 LPS，Low 必须跳过前面 400 的 MPS 空间。\nRange 剧烈缩小到 100。')
    elif frame < 120: # 4-6s: Renormalization
        progress = (frame - 80) / 40.0
        progress = progress * progress * (3 - 2 * progress)
        # Visual renorm: shift back to center, double width
        cur_w = 100 + 100 * progress
        cur_x = 400 - 200 * progress # center the expansion around 400, wait, just expand it
        bar.set_x(cur_x)
        bar.set_width(cur_w)
        bar.set_facecolor('#ef4444')
        text_range.set_text('Range << 1')
        text_range.set_position((cur_x + cur_w/2, 1.5))
        text_low.set_text('Low << 1')
        text_low.set_position((cur_x, 2.2))
        text_title.set_text('第三步：归一化与比特输出 (Renormalization)')
        text_desc.set_text('Range(100) < 256，触发底层硬件左移 (x2)。\nLow 在左移过程中溢出最高位 1，成功写入码流！')
    else: # Hold
        pass

    return bar, text_range, text_low, text_title, text_desc

ani = animation.FuncAnimation(fig, update, frames=140, interval=50, blit=True)
ani.save('cabac_range_anim.gif', writer='pillow', fps=20)
print("GIF generated successfully")
