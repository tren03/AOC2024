# Takes a string and removes newline at the end of the string
def remove_newline(string: str) -> str:
    mod_string = string.removesuffix("\n")
    return mod_string


# Gets the data from the file
def get_data(filepath: str) -> list[str]:
    with open(filepath, "r") as file:
        return file.readlines()


# gets ("str","str") -> we convert to int, find product and return
def calc_prod(nos_tuple: tuple[str, str]) -> int:
    return int(nos_tuple[0]) * int(nos_tuple[1])


import re

if __name__ == "__main__":
    SAMPLE_INPUT_FILE = "../input/sample.txt"
    MAIN_INPUT_FILE = "../input/main.txt"
    sum = 0
    lines = get_data(MAIN_INPUT_FILE)
    for line in lines:
        line_to_process = remove_newline(line)
        print(line_to_process)
        result = re.findall(r"mul\((\d+)\,(\d+)\)", line_to_process)
        if result:
            print(result)
        for tup in result:
            print(calc_prod(tup))
            sum += calc_prod(tup)

    print(sum)
