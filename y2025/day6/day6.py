def solve_day_6_part_1(input: str) -> int:
    def calculate_column(operation: str, numbers_str: list[str]) -> int:
        column_result: int | None = None
        for number_str in numbers_str:
            number = int(number_str)
            if column_result is None:
                column_result = number
            elif operation == "+":
                column_result += number
            elif operation == "*":
                column_result *= number
        if column_result is None:
            return 0
        return column_result

    operation_columns = get_operation_columns(input)
    result = 0
    for operation_column in operation_columns:
        operation = operation_column[-1].strip()
        numbers = operation_column[0:-1]
        result += calculate_column(operation, numbers)
    return result


def solve_day_6_part_2(input: str) -> int:
    def calculate_column(operation: str, numbers_str: list[str]) -> int:
        column_result: int | None = None

        new_numbers_str: list[str] = []
        for number_index in range(len(numbers_str[0])):
            new_number_str = ""
            for number_str in numbers_str:
                new_number_str += number_str[number_index]
            new_numbers_str.append(new_number_str)

        for number_str in new_numbers_str:
            number = int(number_str)
            if column_result is None:
                column_result = number
            elif operation == "+":
                column_result += number
            elif operation == "*":
                column_result *= number
        if column_result is None:
            return 0
        return column_result

    operation_columns = get_operation_columns(input)
    result = 0
    for operation_column in operation_columns:
        operation = operation_column[-1].strip()
        numbers = operation_column[0:-1]
        result += calculate_column(operation, numbers)
    return result


def get_operation_columns(input: str) -> list[list[str]]:
    def get_columns_indices(lines: list[str]) -> list[tuple[int, int]]:
        indices: list[tuple[int, int]] = []
        start_at = 0
        columns_count = len(lines[0])
        for column_index in range(columns_count):
            is_active = any([line[column_index] != " " for line in lines])
            if not is_active:
                indices.append((start_at, column_index - 1))
                start_at = column_index + 1
        indices.append((start_at, columns_count))
        return indices

    lines = [line for line in input.split("\n") if line.strip()]
    columns_indices = get_columns_indices(lines)
    matrix = [
        [
            line[column_indices[0] : column_indices[1] + 1]
            for column_indices in columns_indices
        ]
        for line in lines
    ]
    transposed_matrix = [list(col) for col in zip(*matrix)]

    return transposed_matrix


if __name__ == "__main__":
    with open("y2025/day6/input.txt") as f:
        input = f.read()
    print(solve_day_6_part_1(input))
    print(solve_day_6_part_2(input))
