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


# Testing
# lines: list[str] = get_data("../input/sample.txt")
# mod_lines: list[str] = []
# for line in lines:
#     mod_lines.append(remove_newline(line))
# print(mod_lines)


test_str = "123 123 123"
test_list = get_number_list(test_str)
print(test_list[0] + 1)

