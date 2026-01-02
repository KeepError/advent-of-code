from y2025.day1.day1 import solve_day_1

EXAMPLE_INPUT = """
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""


def test_day_1():
    assert solve_day_1(EXAMPLE_INPUT) == 3
