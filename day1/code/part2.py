# use a hashmap to get occurances of elements in right list, and then just do left_list[i] * hashmap[left_list[i]] (the hashmap gives occurances of left_list element)
from typing import Dict, List, Tuple
from collections import Counter


# Takes a string and removes newline at the end of the string
def remove_newline(string: str) -> str:
    mod_string = string.removesuffix("\n")
    return mod_string


# Gets the data from the file
def get_data(filepath: str) -> List[str]:
    with open(filepath, "r") as file:
        return file.readlines()


# Given a string with two numbers split by some whitespace, gets both numbers and returns them
def get_split_numbers(str_number: str) -> Tuple[int, int]:
    flag: bool = True
    number_1: str = ""
    number_2: str = ""
    for i in str_number:
        try:
            nos: int = int(i)
            if flag == True:
                number_1 += i
            else:
                number_2 += i
        except ValueError:
            # if flag = false, we have finished processing our first number, and we are in second number processing
            flag = False
            continue

    return (int(number_1), int(number_2))


# Takes lines and splits the first and second number in each line into their own arrays, and returns (left_list, hashmap of list of occurances of right arr)
def split_input(clean_lines: List[str]) -> Tuple[List[int], Dict[int, int]]:
    arr1: List[int] = []
    arr2: List[int] = []
    map2: Dict[int, int] = {}
    for line in clean_lines:
        split_numbers: Tuple[int, int] = get_split_numbers(line)
        first_number: int = split_numbers[0]
        second_number: int = split_numbers[1]
        arr1.append(first_number)
        arr2.append(second_number)

    # returns the count of each element
    map2 = Counter(arr2)

    return (arr1, map2)


# finds the differnce between each index of the arrays passed respectively, and returns the sum of differnces
def get_answer(arr1: List[int], map2: Dict[int, int]) -> int:
    answer: int = 0
    print(map2)
    for i in arr1:
        answer += i * map2[i]
    return answer


def main():
    filepath: str = "../input/main.txt"
    lines: List[str] = get_data(filepath)
    clean_lines: List[str] = []
    for line in lines:
        clean_lines.append(remove_newline(line))
    array_tuple: Tuple[List[int], Dict[int, int]] = split_input(clean_lines)
    answer: int = get_answer(array_tuple[0], array_tuple[1])
    print(answer)


main()

# TESTING
# print(get_data("../input/sample.txt"))
# print(remove_newline("hello\n"))
# print(clean_lines)
