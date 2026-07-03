
# --- 1. 导入核心逻辑 ---
from core import build_truth_table, toggle_bit, get_light

# --- 2. 导入可视化函数 ---
# 注意：这里假设 test.py 和 visualize.py 在同一级目录下
from visualize import plot_truth_table_matrix, plot_state_space_graph


def test_truth_table(switch_count: int = 3):
    print("正在打印真值表...")
    for k, v in build_truth_table(switch_count):
        print("".join(map(str, k)), "->", v)
    print("-" * 20)


def test_visualization():

    print("\n正在生成可视化图片...")
    
    # 1. 生成真值表矩阵图
    plot_truth_table_matrix()
    
    # 2. 生成基础状态空间图
    plot_state_space_graph()
    
    # 3. 生成带演示路径的状态空间图
    demo_path = [
        [0, 0, 0],
        [1, 0, 0],
        [1, 1, 0],
        [1, 1, 1]
    ]
    plot_state_space_graph(highlight_path=demo_path)
    
    print("所有图片已生成至 'figures' 文件夹！")
    print("-" * 20)


def test_toggle_bit(switch_count: int = 3):

    switches = [0] * switch_count
    print(f"\n进入交互模式 (初始状态: {switches})")
    print(f"当前灯状态: {get_light(switches)}")
    print(f"输入 0 ~ {switch_count - 1} 来切换对应开关，输入 'q' 退出。")
    
    while True:
        user_input = input(f"\n请输入开关 (0 ~ {switch_count - 1}): ")
        
        if user_input.lower() == 'q':
            print(" 退出程序。")
            break
            
        try:
            toggle = int(user_input)
            if 0 <= toggle < switch_count:
                previous = get_light(switches)
                switches = toggle_bit(switches, toggle)
                current = get_light(switches)
                print(f"状态更新: {switches}, 灯: {previous} -> {current}")
            else:
                print(f"请输入 0 到 {switch_count - 1} 之间的数字。")
        except ValueError:
            print(" 输入无效，请输入一个数字或 'q'。")


if __name__ == "__main__":

    test_truth_table()

    test_visualization()
    
    test_toggle_bit()