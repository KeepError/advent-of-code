def solve_day_7_part_1(input: str) -> int:
    lines = get_lines(input)
    beams: set[int] = set()

    initial_beam = lines[0].find("S")
    beams.add(initial_beam)

    split_counts = 0
    for line in lines[1:]:
        for beam in beams.copy():
            if line[beam] == "^":
                split_counts += 1
                beams.remove(beam)
                beams.add(beam - 1)
                beams.add(beam + 1)

    return split_counts


def solve_day_7_part_2(input: str) -> int:
    return 0


def get_lines(input: str) -> list[str]:
    return input.split()


if __name__ == "__main__":
    with open("y2025/day7/input.txt") as f:
        input = f.read()
    print(solve_day_7_part_1(input))
    print(solve_day_7_part_2(input))
