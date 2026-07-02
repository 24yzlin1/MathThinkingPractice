import random


def generate_bootstrap_sample(data: list[int]) -> list[int]:
    return [data[random.randint(0, len(data) - 1)] for _ in range(len(data))]
