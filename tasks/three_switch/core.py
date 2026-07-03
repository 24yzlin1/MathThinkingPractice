def _parse_value(
    value: int,
    width: int,
) -> list[int]:
    return [
        1 if x == "1" else 0
        for x in format(
            value,
            f"0{width}b",
        )
    ]


def toggle_bit(
    switches: list[int],
    index: int,
) -> list[int]:
    new_switches = switches.copy()
    new_switches[index] = int(not new_switches[index])
    return new_switches


def get_light(switches: list[int]) -> int:
    return sum(switches) % 2


def get_inputs(switch_count: int = 3) -> list[list[int]]:
    return [_parse_value(i, switch_count) for i in range(2**switch_count)]


def build_truth_table(switch_count: int = 3) -> list[tuple[list[int], int]]:
    return [(x, get_light(x)) for x in get_inputs(switch_count)]
