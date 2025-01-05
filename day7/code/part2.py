# total number of operations = +,*,||
# Need to find all combinations of these 3 operations
import re

sym = "++"
s: set[str] = set()


# Takes a string and removes newline at the end of the string
def remove_newline(string: str) -> str:
    """
    Takes a string and returns string without \n
    """
    mod_string = string.removesuffix("\n")
    return mod_string


# Gets the data from the file
def get_data(filepath: str) -> list[str]:
    """
    Read from file and returns each line of the file as a element of list of type string
    """
    with open(filepath, "r") as file:
        return file.readlines()


def rec(i: int, sym: str):
    """
    Recursively get all permutations of chars of string given,
    takes starting index (0) and string to get perms
    """
    if i == len(sym):
        return
    i_true: str = sym
    s.add(i_true)
    temp: str = ""
    temp2: str = ""
    for ind, _ in enumerate(sym):
        if ind == i:
            temp2 += "|"
        else:
            temp2 += sym[ind]

        if ind == i:
            temp += "*"
        else:
            temp += sym[ind]
    i_false: str = temp
    s.add(i_false)
    s.add(temp2)
    rec(i + 1, sym)
    rec(i + 1, temp)
    rec(i + 1, temp2)


def single_calc(nos_list: list[int], operator_str: str) -> int:
    """
    Given a single operator string, calculates the value and returns it
    """
    sum = nos_list[0]
    # index + 1 always exists in nos list as operator_str always has one less element that nos_list
    for index, operator in enumerate(operator_str):
        if operator == "+":
            sum += nos_list[index + 1]
        elif operator == "*":
            sum *= nos_list[index + 1]
        else:
            sum_string = str(sum)
            sum_string_final = sum_string + (str(nos_list[index + 1]))
            sum = int(sum_string_final)
    return sum

def calc(target: int, s: set[str], nos_list: list[int]) -> bool:
    for operator_str in s:
        sum = 0
        sum = single_calc(nos_list, operator_str)
        print("sum = ", sum, type(sum))
        print("target = ", target, type(target))
        if sum == target:
            return True
    return False


# rec(0, sym)
# print(s)
main = "../input/main.txt"
sample = "../input/sample.txt"

data = get_data(main)
clean_data = []
for line in data:
    clean_data.append(remove_newline(line))
print(clean_data)

# regex magic


# regex = r"(\d*):(\S)"
# regex = r"(\d*:((\d*)*))"
# regex = r"^\d+((,\d+)*|( \d+)*)$"
# # regex = r"(^(\d*)$)"
# regex_obj = re.compile(regex)
ans = 0
for d in clean_data:
    nos_list = re.findall(r"[0-9]+", d)
    nos_list_updated: list[int] = []
    for n in nos_list:
        nos_list_updated.append(int(n))

    target = int(nos_list[0])
    nos_list_updated = nos_list_updated[1:]
    # print(target)
    # print(nos_list_updated)
    recursion_op_str = ""
    for i in range(0, len(nos_list_updated) - 1):
        recursion_op_str += "+"
    # print(recursion_op_str)
    print(recursion_op_str)
    s = set()
    rec(0, recursion_op_str)
    if calc(target, s, nos_list_updated):
        ans += target

print(ans)

# print(single_calc([15, 6], "|"))
# rec(0, sym)
# print(s)
