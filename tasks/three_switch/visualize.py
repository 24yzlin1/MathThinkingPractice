
import matplotlib.pyplot as plt
import networkx as nx
import os


try:
    from .core import build_truth_table, toggle_bit, get_light
except ImportError:
    from core import build_truth_table, toggle_bit, get_light


plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# 指定输出目录
OUTPUT_DIR = "figures"


def plot_truth_table_matrix(switch_count=3):

    print("正在生成真值表颜色矩阵...")
    truth_table = build_truth_table(switch_count)
    
    headers = [f"S{i+1}" for i in range(switch_count)] + ["灯状态(L)"]
    table_data = []
    cell_colors = []

    for switches, light in truth_table:
        row_data = switches + [light]
        table_data.append(row_data)
        # 灯亮(1)绿色，灯灭(0)红色，开关列白色
        row_colors = ['#ffffff'] * switch_count + ['#ff9999' if light == 0 else '#99ff99']
        cell_colors.append(row_colors)

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.axis('tight')
    ax.axis('off')
    
    table = ax.table(cellText=table_data,
                     colLabels=headers,
                     cellLoc='center',
                     loc='center')
    
    for i in range(len(table_data)):
        for j in range(len(headers)):
            table[(i+1, j)].set_facecolor(cell_colors[i][j])
            if j == switch_count:
                table[(i+1, j)].set_text_props(weight='bold', color='black')

    table.auto_set_font_size(False)
    table.set_fontsize(12)
    table.scale(1.2, 2)
    
    plt.title(f"三控开关真值表 (共 {2**switch_count} 种状态)", fontsize=16, pad=20)
    
    path = os.path.join(OUTPUT_DIR, "truth_table_matrix.png")
    plt.savefig(path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"已保存: {path}")


def plot_state_space_graph(switch_count=3, highlight_path=None):
   
    print("正在生成状态空间图...")
    truth_table = build_truth_table(switch_count)
    
    G = nx.Graph()
    
    # 1. 添加节点
    for switches, light in truth_table:
        node_id = tuple(switches)
        label = "".join(map(str, switches))
        color = '#66ff66' if light == 1 else '#ff6666'  # 绿亮红灭
        G.add_node(node_id, label=label, color=color)

    # 2. 添加边 (汉明距离为1则连线)
    nodes = list(G.nodes)
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            if sum(a != b for a, b in zip(nodes[i], nodes[j])) == 1:
                G.add_edge(nodes[i], nodes[j])

    pos = nx.shell_layout(G)  # 环形布局，适合3位二进制

    plt.figure(figsize=(10, 8))
    
    node_colors = [G.nodes[n]['color'] for n in G.nodes]
    labels = nx.get_node_attributes(G, 'label')

    nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=800, alpha=0.9)
    nx.draw_networkx_labels(G, pos, labels, font_size=12, font_weight='bold')
    nx.draw_networkx_edges(G, pos, width=1.5, alpha=0.5, edge_color='gray')

    # 3. 高亮路径
    if highlight_path:
        path_edges = [(tuple(highlight_path[k]), tuple(highlight_path[k+1])) 
                      for k in range(len(highlight_path) - 1)]
        
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, width=4, edge_color='blue', alpha=0.8)
        nx.draw_networkx_nodes(G, pos, nodelist=[tuple(p) for p in highlight_path], 
                               node_color='yellow', node_size=900)

    plt.title("三控开关状态空间图\n(绿=亮, 红=灭; 蓝线=演示路径)", fontsize=14)
    plt.axis('off')
    
    suffix = "_path" if highlight_path else ""
    path = os.path.join(OUTPUT_DIR, f"state_space{suffix}.png")
    plt.savefig(path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"已保存: {path}")