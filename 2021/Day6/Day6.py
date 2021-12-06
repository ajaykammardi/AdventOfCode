def read_input(file_name: str) -> list:
    with open(file_name, 'r') as f:
        contents = [int(i) for i in f.read().split(',')]
    return contents


def count_laternfish(fish: list, days: int) -> int:
    fish_counter = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
    for key in fish:
        fish_counter[key] += 1
    for _ in range(days):
        temp_fish_counter = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
        for key in fish_counter:
            temp_fish_counter[key - 1] = fish_counter[key]

        if temp_fish_counter.get(-1):
            temp_fish_counter[8] = temp_fish_counter[-1]
            temp_fish_counter[6] += temp_fish_counter[-1]

        fish_counter = temp_fish_counter
        del temp_fish_counter[-1]

    return sum([value for key, value in fish_counter.items() if value > 0])


def main():
    # To run test cases pass file name as test_case.txt
    file_name = 'input.txt'
    input_list = read_input(file_name)
    print(f"Part 1 -> {count_laternfish(input_list, 80)}")
    print(f"Part 2 -> {count_laternfish(input_list, 256)}")


if __name__ == '__main__':
    main()

