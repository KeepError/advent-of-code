def solve_day_6_part_1(input: str) -> int:
    operation_columns = get_operation_columns(input)
    result = 0
    for operation_column in operation_columns:
        operation = operation_column[1]
        column_result: int | None = None
        for number in operation_column[0]:
            if column_result is None:
                column_result = number
            elif operation == "+":
                column_result += number
            elif operation == "*":
                column_result *= number
        if column_result is not None:
            result += column_result
    return result


def solve_day_6_part_2(input: str) -> int:
    return 0


def get_operation_columns(input: str) -> list[tuple[list[int], str]]:
    lines = [line for line in input.strip().split("\n") if line.strip()]

    number_lines = lines[:-1]
    operator_line = lines[-1]

    operators = operator_line.split()

    number_matrix = [line.split() for line in number_lines]

    transposed_numbers = zip(*number_matrix)

    result = []

    for col_tuple, op in zip(transposed_numbers, operators):
        col_ints = [int(num) for num in col_tuple]
        result.append((col_ints, op))

    return result


if __name__ == "__main__":
    with open("y2025/day6/input.txt") as f:
        input = f.read()
    print(solve_day_6_part_1(input))
    print(solve_day_6_part_2(input))
