def solve_day_3(input: str) -> int:
    banks = input.split()
    return sum([get_largest_joltage(bank) for bank in banks])


DIGITS_COUNT = 12


battery_entries_type = list[tuple[int, int]]


def get_largest_joltage(bank: str) -> int:
    battery_entries: battery_entries_type = list(
        enumerate([int(battery_str) for battery_str in bank])
    )
    active_sorted_battery_entries: battery_entries_type = sorted(
        battery_entries, key=lambda entry: (-entry[1], entry[0])
    )
    result_battery_entries: battery_entries_type = []
    while len(result_battery_entries) < DIGITS_COUNT:
        add_battery_entry_to_result(
            result_battery_entries, active_sorted_battery_entries
        )
    return sum(
        [
            battery_entry[1] * (10 ** (DIGITS_COUNT - i - 1))
            for i, battery_entry in enumerate(result_battery_entries)
        ]
    )


def add_battery_entry_to_result(
    result_battery_entries: battery_entries_type,
    sorted_battery_entries: list[tuple[int, int]],
):
    for i, battery_entry in enumerate(sorted_battery_entries):
        battery_i, battery = battery_entry

        if result_battery_entries and battery_i <= result_battery_entries[-1][0]:
            continue

        bank_batteries_left_with_current = len(sorted_battery_entries) - battery_i
        result_batteries_left = DIGITS_COUNT - len(result_battery_entries)
        if bank_batteries_left_with_current < result_batteries_left:
            continue
        result_battery_entries.append(battery_entry)
        break


if __name__ == "__main__":
    with open("y2025/day3/input.txt") as f:
        input = f.read()
    print(solve_day_3(input))
