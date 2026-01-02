def solve_day_2(input: str) -> int:
    num_ranges = input.split(",")
    invalid_nums: list[int] = []
    for num_range in num_ranges:
        start_num, end_num = map(int, num_range.split("-"))
        for current_num in range(start_num, end_num + 1):
            if is_invalid(current_num):
                invalid_nums.append(current_num)
    return sum(invalid_nums)


def is_invalid(num: int) -> bool:
    num_str = str(num)
    if len(num_str) % 2 != 0:
        return False
    first_part = num_str[: len(num_str) // 2]
    second_part = num_str[len(num_str) // 2 :]
    return first_part == second_part


if __name__ == "__main__":
    with open("y2025/day2/input.txt") as f:
        input = f.read()
    print(solve_day_2(input))
