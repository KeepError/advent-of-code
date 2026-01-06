def solve_day_5_part_1(input: str) -> int:
    fresh_ingredient_ranges, available_ingredients = (
        get_fresh_ingredients_and_available_ingredients_from_input(input)
    )

    result = 0
    for ingredient in available_ingredients:
        for start, stop in fresh_ingredient_ranges:
            if ingredient >= start and ingredient <= stop:
                result += 1
                break
    return result


def solve_day_5_part_2(input: str) -> int:
    fresh_ingredient_ranges, available_ingredients = (
        get_fresh_ingredients_and_available_ingredients_from_input(input)
    )
    fresh_ingredient_ranges.sort(key=lambda ingredient_range: ingredient_range[0])

    result = 0
    max_stop = -1
    for start, stop in fresh_ingredient_ranges:
        start = max(start, max_stop + 1)
        result += max(0, stop - start + 1)
        max_stop = max(max_stop, stop)
    return result


def get_fresh_ingredients_and_available_ingredients_from_input(
    input: str,
) -> tuple[list[tuple[int, int]], list[int]]:
    fresh_ingredients: list[tuple[int, int]] = []
    available_ingredients: list[int] = []

    lines = [line.strip() for line in input.strip().splitlines()]

    separator_index = lines.index("")

    # Parse ranges
    for line in lines[:separator_index]:
        start, end = line.split("-")
        fresh_ingredients.append((int(start), int(end)))

    # Parse available ingredients
    for line in lines[separator_index + 1 :]:
        available_ingredients.append(int(line))

    return fresh_ingredients, available_ingredients


if __name__ == "__main__":
    with open("y2025/day5/input.txt") as f:
        input = f.read()
    print(solve_day_5_part_1(input))
    print(solve_day_5_part_2(input))
