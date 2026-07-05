
import matplotlib.pyplot as plt
import networkx as nx
import os


try:
    from .core import build_truth_table, toggle_bit, get_light
except ImportError:
    from core import build_truth_table, toggle_bit, get_light


plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "figures")


def plot_truth_table_matrix(switch_count=3):

    print("Generating truth table color matrix...")
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
    plt.show()
    plt.close()
    print(f"Saved: {path}")


def plot_state_space_graph(switch_count=3, highlight_path=None):

    print("Generating state space graph...")
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
    plt.show()
    plt.close()
    print(f"Saved: {path}")

def plot_output_state_distribution(switch_count=3):

    print("Generating output state distribution chart...")
    truth_table = build_truth_table(switch_count)
    
    # 统计亮灭数量
    count_on = sum(1 for _, light in truth_table if light == 1)
    count_off = len(truth_table) - count_on
    
    labels = [f'Light OFF (L=0) - {count_off} states', f'Light ON (L=1) - {count_on} states']
    sizes = [count_off, count_on]
    colors = ['#ff9999', '#99ff99'] # 与你真值表中的颜色保持一致
    
    plt.figure(figsize=(8, 8))
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%',
            shadow=True, startangle=140, textprops={'fontsize': 12})
    plt.title("Output State Distribution\n(Light ON vs OFF Ratio)", fontsize=14)
    plt.axis('equal')  # 保证饼图是正圆
    
    save_path = os.path.join(OUTPUT_DIR, 'result_output_distribution.png')
    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.show()
    plt.close()
    print(f"Saved: {save_path}")

def plot_correctness_verification_table(switch_count=3):

    print("Generating correctness verification table...")
    truth_table = build_truth_table(switch_count)
    

    table_data = []
    for switches, light in truth_table:
        # 理论值：三控开关理论就是奇偶校验
        theoretical = sum(switches) % 2
        # 实际值：来自核心逻辑
        actual = light
        # 验证结果
        is_correct = theoretical == actual
        row = [
            f"{switches[0]}", f"{switches[1]}", f"{switches[2]}",
            str(theoretical), str(actual), 
            "PASS" if is_correct else "FAIL"
        ]
        table_data.append(row)
        
    plt.figure(figsize=(10, 6))
    plt.axis('off')
    
    col_labels = ['S1', 'S2', 'S3', 'Theoretical', 'Actual Code', 'Verification']
    
    table = plt.table(cellText=table_data, colLabels=col_labels, loc='center', cellLoc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(12)
    table.scale(1.2, 1.8)
    
    # 样式美化
    for j in range(len(col_labels)):
        table[0, j].set_facecolor("#4CAF50")  # 表头绿色
        table[0, j].set_text_props(color="white", fontweight='bold')
        
    for i in range(len(truth_table)):
        if table_data[i][5] == "PASS ✔":
            table[i+1, 5].set_facecolor("#C8E6C9")  # PASS 浅绿
        else:
            table[i+1, 5].set_facecolor("#FFCDD2")  # FAIL 浅红
            
    plt.title("Correctness Verification Table\n(Theoretical vs Actual Code Output)", fontsize=14, pad=20)
    
    save_path = os.path.join(OUTPUT_DIR, 'result_correctness_verification.png')
    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.show()
    plt.close()
    print(f"Saved: {save_path}")