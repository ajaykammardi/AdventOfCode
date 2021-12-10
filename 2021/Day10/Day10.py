def read_input(file_name: str) -> list:
    with open(file_name, 'r') as f:
        contents = [i.strip() for i in f.readlines()]
    return contents


def find_illegal_character(chunks: list) -> int:
    character_score = {')': 3, ']': 57, '}': 1197, '>': 25137}
    open_character = {'(': ')', '[': ']', '{': '}', '<': '>'}
    illegal_character_count = 0
    for chunk in chunks:
        temp_queue = []
        for character in chunk:
            if character in open_character:
                temp_queue.append(character)
            else:
                key = temp_queue.pop()
                if open_character.get(key) != character:
                    illegal_character_count += character_score.get(character)
                    break
    return illegal_character_count


def find_incomplete_character(chunks: list) -> int:
    character_score = {')': 1, ']': 2, '}': 3, '>': 4}
    open_character = {'(': ')', '[': ']', '{': '}', '<': '>'}
    incomplete_characters_scores = []
    for chunk in chunks:
        temp_queue = []
        for character in chunk:
            if character in open_character:
                temp_queue.append(character)
            else:
                key = temp_queue.pop()
                if open_character.get(key) != character:
                    break

        else:
            total_score = 0
            for i in temp_queue[::-1]:
                total_score = 5*total_score + character_score.get(open_character.get(i))
            incomplete_characters_scores.append(total_score)
    incomplete_characters_scores.sort()
    mid = len(incomplete_characters_scores)//2
    return incomplete_characters_scores[mid]


def main():
    # To run test cases pass file name as test_case.txt
    file_name = 'input.txt'
    input_list = read_input(file_name)
    print(f"Part 1 -> {find_illegal_character(input_list)}")
    print(f"Part 2 -> {find_incomplete_character(input_list)}")


if __name__ == '__main__':
    main()