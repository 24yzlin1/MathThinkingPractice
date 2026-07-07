import tasks.iterative.test as t1
import tasks.three_switch.test as t2
import tasks.bootstrap.test as t3


def main():
    print("Hello from math-thinking-practice!")

    print()
    print()

    print("=== Task 1: Iterative Methods for Linear Systems ===")
    print("--- Testing set1 ---")
    t1.test_iterative_methods(t1.set1)
    t1.test_plot(t1.set1, "set1")
    print()

    print("--- Testing set2 ---")
    t1.test_iterative_methods(t1.set2)
    t1.test_plot(t1.set2, "set2")
    print()

    print("--- Testing set3 ---")
    t1.test_iterative_methods(t1.set3)
    t1.test_plot(t1.set3, "set3")

    print()
    print()

    print("=== Task 2: Three-Switch Logic ===")
    t2.test_truth_table()
    t2.test_visualization()
    t2.test_toggle_bit()

    print()
    print()

    print("=== Task 3: Bootstrap Estimation ===")
    t3.test_bootstrap_workflow(iterations=100)
    t3.test_bootstrap_workflow(iterations=500)
    t3.test_bootstrap_workflow(iterations=1000)


if __name__ == "__main__":
    main()
