import math


def read_input(file_name: str) -> list:
    with open(file_name, 'r') as f:
        contents = [int(i) for i in f.read().split(',')]
    return contents


def compute_fuel_cost(crab_positions: list) -> int:
    crab_positions_with_fuel_cost = dict.fromkeys(crab_positions, 0)
    for position in crab_positions_with_fuel_cost:
        crab_positions_with_fuel_cost[position] = sum([abs(i-position)for i in crab_positions])

    return min(crab_positions_with_fuel_cost.values())


def compute_fuel_cost_part2(crab_positions: list) -> int:
    min_fuel_consumption = math.inf
    for position in range(max(crab_positions)+1):
        current_fuel = sum([(abs(i-position) * (abs(i-position)+1))//2 for i in crab_positions])
        min_fuel_consumption = min(current_fuel, min_fuel_consumption)

    return min_fuel_consumption


def main():
    # To run test cases pass file name as test_case.txt
    file_name = 'input.txt'
    input_list = read_input(file_name)
    print(f"Part 1 -> {compute_fuel_cost(input_list)}")
    print(f"Part 1 -> {compute_fuel_cost_part2(input_list)}")


if __name__ == '__main__':
    main()
