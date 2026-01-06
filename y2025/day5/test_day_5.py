from y2025.day5.day5 import (
    get_fresh_ingredients_and_available_ingredients_from_input,
    solve_day_5_part_1,
)

EXAMPLE_INPUT = """
3-5
10-14
16-20
12-18

1
5
8
11
17
32
"""


def test_day_5():
    assert solve_day_5_part_1(EXAMPLE_INPUT) == 3
    # assert solve_day_5_part_2(EXAMPLE_INPUT) == 43

    assert get_fresh_ingredients_and_available_ingredients_from_input(
        EXAMPLE_INPUT
    ) == ([(3, 5), (10, 14), (16, 20), (12, 18)], [1, 5, 8, 11, 17, 32])
