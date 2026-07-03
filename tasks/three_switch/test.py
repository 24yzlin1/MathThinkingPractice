from core import *


def test_truth_table(switch_count: int = 3):
    for k, v in build_truth_table(switch_count):
        print("".join(map(str, k)), "->", v)


def test_toggle_bit(switch_count: int = 3):
    switches = [0] * switch_count
    print(f"Switches: {switches}, Light: {get_light(switches)}")
    print("Press Ctrl+C to exit.")
    print()

    while True:
        toggle = int(input(f"Enter switch index to toggle (0 ~ {switch_count - 1}): "))
        previous = get_light(switches)
        switches = toggle_bit(switches, toggle)
        current = get_light(switches)
        print(f"Switches: {switches}, Light: {previous} -> {current}")
        print()


if __name__ == "__main__":
    test_toggle_bit()
