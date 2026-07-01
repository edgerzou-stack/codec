import graphviz

dot = graphviz.Digraph(comment='CABAC Encoder/Decoder Architecture', format='svg')
dot.attr(rankdir='TB', size='10,12', fontname='Inter')
dot.attr('node', fontname='Inter', shape='box', style='rounded,filled', fillcolor='#f8fafc', color='#cbd5e1', penwidth='2')
dot.attr('edge', fontname='Inter', color='#64748b', fontsize='11')

# Encoder Subgraph
with dot.subgraph(name='cluster_encoder') as enc:
    enc.attr(label='编码端流水线 (Encoder)', style='dashed', color='#38bdf8', fillcolor='#f0f9ff', fontcolor='#0369a1', fontname='Inter', fontsize='14')
    enc.node('SE_E', '语法元素\ne.g. MVD=1', fillcolor='#e0f2fe', color='#38bdf8', fontcolor='#0369a1')
    enc.node('BIN_E', 'Bin 数组\n[1, 0, 0]', fillcolor='#e0f2fe', color='#38bdf8', fontcolor='#0369a1')
    enc.node('BITS_E', '纯比特流\n01011...', fillcolor='#fee2e2', color='#f87171', fontcolor='#b91c1c')
    
    enc.edge('SE_E', 'BIN_E', label=' 1. 二值化')
    enc.edge('BIN_E', 'BITS_E', label=' 2. 算术编码')

dot.node('BITS_D', '物理比特流\n01011...', fillcolor='#fee2e2', color='#f87171', fontcolor='#b91c1c')
dot.edge('BITS_E', 'BITS_D', label=' 网络传输 / 硬盘存储')

# Decoder Subgraph
with dot.subgraph(name='cluster_decoder') as dec:
    dec.attr(label='解码端微观死循环: Bin-by-Bin Decoding', style='dashed', color='#4ade80', fillcolor='#f0fdf4', fontcolor='#15803d', fontname='Inter', fontsize='14')
    
    dec.node('FSM', '1. 顶层状态机 FSM\n决定当前要解什么\ne.g. MVD', fillcolor='#dcfce7', color='#4ade80', fontcolor='#15803d', shape='hexagon')
    dec.node('CTX', '2. Context 模型\n查表给出下一个 Bin 的概率', fillcolor='#fef08a', color='#eab308', fontcolor='#854d0e')
    dec.node('ARITH', '3. 算术解码引擎\n吃进 Bit, 吐出 1 个 Bin', fillcolor='#fef08a', color='#eab308', fontcolor='#854d0e')
    dec.node('MATCH', '4. 反二值化匹配\n收集 Bin 并尝试组合', fillcolor='#fef08a', color='#eab308', fontcolor='#854d0e', shape='diamond')
    dec.node('SE_OUT', '5. 成功解析！\n输出完整语法元素\ne.g. MVD=1', fillcolor='#dcfce7', color='#4ade80', fontcolor='#15803d')

    dec.edge('FSM', 'CTX', label='请求解码下一个 Bin')
    dec.edge('CTX', 'ARITH', label='提供概率 p0/p1')
    dec.edge('ARITH', 'MATCH', label="解出 1 个 Bin\n(e.g. '1')")
    dec.edge('MATCH', 'CTX', label='前缀不完整\n继续要下一个 Bin')
    dec.edge('MATCH', 'SE_OUT', label='符合码表规则\n组合成功！')
    dec.edge('SE_OUT', 'FSM', label='通知 FSM\n进入下一个语法元素')

dot.edge('BITS_D', 'ARITH', label='提供纯数据', style='dashed')

dot.render('cabac_arch_diagram', cleanup=True)
