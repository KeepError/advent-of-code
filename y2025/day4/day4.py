def solve_day_4_part_1(input: str) -> int:
    rows = [list(row) for row in input.split()]
    rolls_to_remove = get_rolls_to_remove(rows)
    return len(rolls_to_remove)


def solve_day_4_part_2(input: str) -> int:
    rows = [list(row) for row in input.split()]
    result = 0
    while True:
        rolls_to_remove = get_rolls_to_remove(rows)
        result += len(rolls_to_remove)
        if len(rolls_to_remove) == 0:
            break
        for roll in rolls_to_remove:
            y, x = roll
            rows[y][x] = "."
    return result


def get_rolls_to_remove(rows: list[list[str]]) -> list[tuple[int, int]]:
    result: list[tuple[int, int]] = []
    for y in range(len(rows)):
        for x in range(len(rows[y])):
            if rows[y][x] == "@" and get_adjacent_rolls_count(rows, y, x) < 4:
                result.append((y, x))
    return result


def get_adjacent_rolls_count(rows: list[list[str]], y: int, x: int) -> int:
    res = 0
    for cur_y in range(y - 1, y + 1 + 1):
        for cur_x in range(x - 1, x + 1 + 1):
            if cur_y == y and cur_x == x:
                continue
            if cur_y < 0 or cur_y >= len(rows):
                continue
            if cur_x < 0 or cur_x >= len(rows[cur_y]):
                continue
            if rows[cur_y][cur_x] != "@":
                continue
            res += 1
    return res


if __name__ == "__main__":
    with open("y2025/day4/input.txt") as f:
        input = f.read()
    print(solve_day_4_part_1(input))
    print(solve_day_4_part_2(input))
