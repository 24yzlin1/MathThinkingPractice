
from core import build_truth_table, toggle_bit, get_light

from visualize import plot_truth_table_matrix, plot_state_space_graph, plot_output_state_distribution, plot_correctness_verification_table


def test_truth_table(switch_count: int = 3):
    print("Printing truth table...")
    for k, v in build_truth_table(switch_count):
        print("".join(map(str, k)), "->", v)
    print("-" * 20)


def test_visualization():

    print("\nGenerating visualization images...")

    plot_truth_table_matrix()

    plot_state_space_graph()

    demo_path = [
        [0, 0, 0],
        [1, 0, 0],
        [1, 1, 0],
        [1, 1, 1]
    ]
    plot_state_space_graph(highlight_path=demo_path)

    print("All images saved to 'figures' folder!")
    print("-" * 20)


def test_toggle_bit(switch_count: int = 3):

    switches = [0] * switch_count
    print(f"\nEnter interactive mode (initial state: {switches})")
    print(f"Current light state: {get_light(switches)}")
    print(f"Input 0 ~ {switch_count - 1} to toggle switch, 'q' to quit.")

    while True:
        user_input = input(f"\nEnter switch (0 ~ {switch_count - 1}): ")

        if user_input.lower() == 'q':
            print("Exit program.")
            break

        try:
            toggle = int(user_input)
            if 0 <= toggle < switch_count:
                previous = get_light(switches)
                switches = toggle_bit(switches, toggle)
                current = get_light(switches)
                print(f"State updated: {switches}, Light: {previous} -> {current}")
            else:
                print(f"Please enter a number between 0 and {switch_count - 1}.")
        except ValueError:
            print("Invalid input, please enter a number or 'q'.")


if __name__ == "__main__":
    test_truth_table()
    test_visualization()
    plot_output_state_distribution()
    plot_correctness_verification_table()
    test_toggle_bit()