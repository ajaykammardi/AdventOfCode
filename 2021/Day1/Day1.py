def read_input(file_name: str) -> list:
    with open(file_name, 'r') as f:
        contents = [int(i.strip()) for i in f.readlines()]
    return contents


def count_of_depth_increase(nums: list) -> int:
    count = sum([1 for i in range(0, len(nums)-1) if (nums[i+1] > nums[i])])
    return count


def count_of_depth_increase_part_two(nums: list) -> int:
    temp_list = [sum(nums[i-3:i]) for i in range(3, len(nums)+1)]
    count = count_of_depth_increase(temp_list)
    return count


def main():
    # To run test cases pass file name as test_case.txt
    file_name = 'input.txt'
    input_list = read_input(file_name)
    print(f"Part 1 -> {count_of_depth_increase(input_list)}")
    print(f"Part 2 -> {count_of_depth_increase_part_two(input_list)}")


if __name__ == '__main__':
    main()
