def read_input(file_name: str) -> list:
    with open(file_name, 'r') as f:
        contents = [list(i.strip()) for i in f.readlines()]
    return contents


def compute_power_consumption(logs: list) -> int:
    transposed_logs = list(map(list, zip(*logs)))
    gamma = ''

    for log in transposed_logs:
        if log.count('1') > len(log)//2:
            gamma += '1'
        else:
            gamma += '0'

    epsilon = ''.join(['1' if i == '0' else '0' for i in gamma])
    return int(gamma,2)*int(epsilon,2)


def main():
    # To run test cases pass file name as test_case.txt
    file_name = 'input.txt'
    input_list = read_input(file_name)
    print(f"Part 1 -> {compute_power_consumption(input_list)}")


if __name__ == '__main__':
    main()