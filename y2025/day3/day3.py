def solve_day_3(input: str) -> int:
    banks = input.split()
    return sum([get_largest_joltage(bank) for bank in banks])


def get_largest_joltage(bank: str) -> int:
    max_first = 0
    max_second = -1
    for i in range(len(bank)):
        battery = int(bank[i])
        if battery > max_first and i != len(bank) - 1:
            max_second = -1
            max_first = battery
        elif battery > max_second:
            max_second = battery
    return max_first * 10 + max_second


if __name__ == "__main__":
    with open("y2025/day3/input.txt") as f:
        input = f.read()
    print(solve_day_3(input))
