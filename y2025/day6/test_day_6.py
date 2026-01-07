from y2025.day6.day6 import (
    get_operation_columns,
    solve_day_6_part_1,
    solve_day_6_part_2,
)

EXAMPLE_INPUT = """
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
"""


def test_day_6():
    assert solve_day_6_part_1(EXAMPLE_INPUT) == 4277556
    assert solve_day_6_part_2(EXAMPLE_INPUT) == 0

    assert get_operation_columns(EXAMPLE_INPUT) == [
        ([123, 45, 6], "*"),
        ([328, 64, 98], "+"),
        ([51, 387, 215], "*"),
        ([64, 23, 314], "+"),
    ]
