from y2025.day4.day4 import solve_day_4_part_1, solve_day_4_part_2

EXAMPLE_INPUT = """
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
"""


def test_day_4():
    assert solve_day_4_part_1(EXAMPLE_INPUT) == 13
    assert solve_day_4_part_2(EXAMPLE_INPUT) == 43
