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


def compute_o2_co2_rating(logs: list) -> int:
    o2_logs = logs.copy()
    co2_logs = logs.copy()

    transposed_o2_logs = list(map(list, zip(*o2_logs)))
    i = 0
    while len(o2_logs) > 1:
        if transposed_o2_logs[i].count('1') >= len(transposed_o2_logs[i])/2:
            bits = '1'
        else:
            bits = '0'
        o2_logs = list(filter(lambda x: x[i] == bits, o2_logs))
        transposed_o2_logs = list(map(list, zip(*o2_logs)))
        i += 1

    transposed_co2_logs = list(map(list, zip(*co2_logs)))
    i = 0
    while len(co2_logs) > 1:
        if transposed_co2_logs[i].count('1') >= len(transposed_co2_logs[i]) / 2:
            bits = '0'
        else:
            bits = '1'
        co2_logs = list(filter(lambda x: x[i] == bits, co2_logs))
        transposed_co2_logs = list(map(list, zip(*co2_logs)))
        i += 1

    return int(''.join(o2_logs[0]),2)*int(''.join(co2_logs[0]),2)




def main():
    # To run test cases pass file name as test_case.txt
    file_name = 'input.txt'
    input_list = read_input(file_name)
    print(f"Part 1 -> {compute_power_consumption(input_list)}")
    print(f"Part 2 -> {compute_o2_co2_rating(input_list)}")


if __name__ == '__main__':
    main()