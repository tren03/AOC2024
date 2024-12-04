# Get data from filepath
def get_data(filepath: str) -> list[str]:
    with open(filepath, "r") as f:
        return f.readlines()


# Takes a string and removes newline at the end of the string
def remove_newline(string: str) -> str:
    mod_string = string.removesuffix("\n")
    return mod_string


# Given a string of space seperated numbers, return all the numbers as a list of integers
def get_number_list(nos_list: str) -> list[int]:
    # indicates we reached a new number
    flag: bool = True

    temp_string_nos: str = ""
    arr_list: list[int] = []
    for i in nos_list:
        try:
            nos = int(i)
            flag = True
            temp_string_nos += i
        except ValueError:
            flag = False

        # we have reached blank space
        if flag == False:
            nos_to_add = int(temp_string_nos)
            arr_list.append(nos_to_add)
            temp_string_nos = ""
        else:
            continue

    arr_list.append(int(temp_string_nos))

    return arr_list


# So, a report only counts as safe if both of the following are true:
# The levels are either all increasing or all decreasing.
# Any two adjacent levels differ by at least one and at most three.
def validator(nos_list: list[int]) -> bool:
    # we assume that numbers are not in ascending
    is_asc = True
    nos1 = nos_list[0]
    nos2 = nos_list[1]

    if nos1 == nos2:
        return False
    if nos1 > nos2:
        is_asc = False

    # print(is_asc)
    for index in range(1, len(nos_list)):
        nos_prev = nos_list[index - 1]
        nos_cur = nos_list[index]
        diff = abs(nos_cur - nos_prev)
        # print(f"diff inside for : {diff}")
        # print(f"cur number {nos_cur}")
        if (diff < 1) or (diff > 3):
            return False

        if is_asc:
            # When ascending the prev should always be smaller than cur
            if nos_prev >= nos_cur:
                return False
        else:
            # When descending the prev should always be greater than cur
            if nos_prev <= nos_cur:
                return False

    return True


def main():
    lines: list[str] = get_data("../input/main.txt")
    counter = 0
    for line in lines:
        mod_line = remove_newline(line)
        mod_line_nos = get_number_list(mod_line)
        if validator(mod_line_nos):
            counter += 1

    print(counter)

    pass


main()


# Testing
# mod_lines: list[str] = []
# for line in lines:
#     mod_lines.append(remove_newline(line))
# print(mod_lines)

# test_str = "123 123 123"
# test_list = get_number_list(test_str)
# print(test_list)
# print(validator([1, 2, 7, 8, 9]))
