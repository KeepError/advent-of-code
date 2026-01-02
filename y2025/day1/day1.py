def solve_day_1(input: str) -> int:
    rotations = input.split()
    limit = 100
    current = 50
    amount_0 = 0
    for rotation in rotations:
        direction = rotation[0]
        amount = int(rotation[1:])
        if direction == "L":
            amount = 0 - amount
        current += amount
        current = current % limit
        if current == 0:
            amount_0 += 1
    return amount_0


if __name__ == "__main__":
    with open("y2025/day1/input.txt") as f:
        input = f.read()
    print(solve_day_1(input))
