def read_input(file_name: str) -> list:
    with open(file_name, 'r') as f:
        contents = [i.strip()for i in f.readlines()]
        bingo_drawn = [int(i) for i in contents[0].split(',')]
        bingo_tickets = []
        temp = []
        for i in contents[2:]:
            if len(i) != 0:
                temp.append([int(i) for i in (i.strip().replace('  ', ',').replace(' ', ',').split(','))])
            else:
                bingo_tickets.append(temp)
                temp = []
        bingo_tickets.append(temp)
    return bingo_drawn, bingo_tickets


def main():
    # To run test cases pass file name as test_case.txt
    file_name = 'test_case.txt'
    input_list = read_input(file_name)
    print(input_list)


if __name__ == '__main__':
    main()