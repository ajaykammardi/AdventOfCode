from itertools import product


def read_input(file_name: str) -> list:
    with open(file_name, 'r') as f:
        contents = [[int(j) for j in i.strip()] for i in f.readlines()]
    return contents


def get_adjacent_locations(data: list, row: int, col: int) -> list:
    location_to_scan = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    adjacent_locations = []
    for row_to_add, col_to_add in location_to_scan:
        nxt_row = row + row_to_add
        nxt_col = col + col_to_add
        if 0 <= nxt_row < len(data) and 0 <= nxt_col < len(data[0]):
            adjacent_locations.append((nxt_row, nxt_col))
    return adjacent_locations


def compute_risk_level(heatmap: list) -> int:
    risk_position = []

    for row, col in product(range(len(heatmap)), range(len(heatmap[0]))):
        adjacent = get_adjacent_locations(heatmap, row, col)
        if all(heatmap[row][col] < heatmap[adj_row][adj_col] for adj_row, adj_col in adjacent):
            risk_position.append(heatmap[row][col]+1)
    return sum(risk_position)


def main():
    # To run test cases pass file name as test_case.txt
    file_name = 'input.txt'
    input_list = read_input(file_name)
    print(f"Part 1 -> {compute_risk_level(input_list)}")


if __name__ == '__main__':
    main()