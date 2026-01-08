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
    def add_beam_timeline(
        beam_timelines: dict[int, int], beam_timeline: int, value: int
    ):
        beam_timelines[beam_timeline] = beam_timelines.get(beam_timeline, 0) + value

    lines = get_lines(input)
    beam_timelines: dict[int, int] = {}

    initial_beam = lines[0].find("S")
    beam_timelines[initial_beam] = 1

    for line in lines[1:]:
        new_beam_timelines: dict[int, int] = {}
        for beam_timeline in beam_timelines:
            if line[beam_timeline] != "^":
                add_beam_timeline(
                    new_beam_timelines, beam_timeline, beam_timelines[beam_timeline]
                )
                continue
            add_beam_timeline(
                new_beam_timelines, beam_timeline - 1, beam_timelines[beam_timeline]
            )
            add_beam_timeline(
                new_beam_timelines, beam_timeline + 1, beam_timelines[beam_timeline]
            )
        beam_timelines = new_beam_timelines

    return sum(beam_timelines.values())


def get_lines(input: str) -> list[str]:
    return input.split()


if __name__ == "__main__":
    with open("y2025/day7/input.txt") as f:
        input = f.read()
    print(solve_day_7_part_1(input))
    print(solve_day_7_part_2(input))
