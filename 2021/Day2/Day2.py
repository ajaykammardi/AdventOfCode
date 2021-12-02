def read_input(file_name: str) -> list:
    with open(file_name, 'r') as f:
        contents = [(i.strip().split()[0], int(i.strip().split()[1])) for i in f.readlines()]
    return contents


def final_position(positions: list) -> int:
    horizontal = 0
    depth = 0
    for position in positions:
        if position[0] == 'forward':
            horizontal += position[1]
        elif position[0] == 'up':
            depth -= position[1]
        elif position[0] == 'down':
            depth += position[1]
    return horizontal*depth


def final_position_with_aim(positions: list) -> int:
    horizontal = 0
    depth = 0
    aim = 0
    for position in positions:
        if position[0] == 'forward':
            horizontal += position[1]
            depth += aim*position[1]
        elif position[0] == 'up':
            aim -= position[1]
        elif position[0] == 'down':
            aim += position[1]
    return horizontal*depth


def main():
    # To run test cases pass file name as test_case.txt
    file_name = 'input.txt'
    input_list = read_input(file_name)
    print(f"Part 1 -> {final_position(input_list)}")
    print(f"Part 1 -> {final_position_with_aim(input_list)}")


if __name__ == '__main__':
    main()