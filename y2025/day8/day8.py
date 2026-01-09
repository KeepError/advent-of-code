import math


def solve_day_8_part_1(connections: int, input: str) -> int:
    junction_boxes = get_junction_boxes(input)

    distances: dict[tuple[int, int], float] = {}
    for jb_i in range(len(junction_boxes)):
        for jb_j in range(len(junction_boxes)):
            if jb_i >= jb_j:
                continue
            distances[(jb_i, jb_j)] = get_junction_boxes_distance(
                junction_boxes[jb_i], junction_boxes[jb_j]
            )

    sorted_junction_boxes = sorted(
        distances.keys(), key=lambda dist_key: distances[dist_key]
    )

    circuits: dict[int, set[int]] = {
        jb_i: {jb_i} for jb_i in range(len(junction_boxes))
    }
    for jb_i, jb_j in sorted_junction_boxes[:connections]:
        jbs_to_update = tuple(circuits[jb_j])
        circuits[jb_i].update(circuits[jb_j])
        for jb in jbs_to_update:
            circuits[jb] = circuits[jb_i]

    circuits_sizes: list[int] = []
    excluded_jbs: set[int] = set()
    for jb, circuit in circuits.items():
        if jb in excluded_jbs:
            continue
        circuits_sizes.append(len(circuit))
        excluded_jbs.update(circuit)

    largest_circuits_sizes = sorted(circuits_sizes, reverse=True)

    result = 1
    for circuit_size in largest_circuits_sizes[:3]:
        result *= circuit_size

    return result


def solve_day_8_part_2(input: str) -> int:
    return 0


junction_box_type = tuple[int, int, int]


def get_junction_boxes(input: str) -> list[junction_box_type]:
    lines = input.strip().split()
    junction_boxes: list[junction_box_type] = []
    for line in lines:
        nums_str = line.split(",")
        nums = list(map(int, nums_str))
        junction_boxes.append(tuple(nums[:3]))
    return junction_boxes


def get_junction_boxes_distance(
    junction_box_1: junction_box_type, junction_box_2: junction_box_type
) -> float:
    return math.sqrt(
        (junction_box_1[0] - junction_box_2[0]) ** 2
        + (junction_box_1[1] - junction_box_2[1]) ** 2
        + (junction_box_1[2] - junction_box_2[2]) ** 2
    )


if __name__ == "__main__":
    with open("y2025/day8/input.txt") as f:
        input = f.read()
    print(solve_day_8_part_1(1000, input))
    print(solve_day_8_part_2(input))
