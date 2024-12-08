# need to find a, check diagonals, and check is set containes 2 M and 2 S


def remove_newline(string: str) -> str:
    """
    Takes a string and removes newline at the end of the string
    """
    mod_string = string.removesuffix("\n")
    return mod_string


def get_data(filepath: str) -> list[str]:
    """
    Gets the data from the file
    """
    with open(filepath, "r") as file:
        return file.readlines()


def convert_to_2d_matix(str_list: list[str]) -> list[list[str]]:
    """
    Takes a list[str] and converts in into a 2d matrix where
    each element is a char
    """
    row = 0
    col = 0
    matrix = [[""] * DIM for i in range(DIM)]
    # print(matrix)
    for line in str_list:
        col = 0
        for char in line:
            matrix[row][col] = char
            col += 1
        row += 1

    return matrix


def is_index_valid(index: tuple[int, int]) -> bool:
    """
    returns true if index is valid, else false
    """
    if index[0] < DIM and index[0] >= 0 and index[1] < DIM and index[1] >= 0:
        return True
    return False


def diagonal_check(matrix: list[list[str]], index: tuple[int, int]) -> int:
    """
    We get passed index if a, store all diagonals in a hashmap and check if containes 2m and 2s
    """
    cur_row = index[0]
    cur_col = index[1]

    count = {}

    top_left = ""
    top_right = ""
    bottom_right = ""
    bottom_left = ""

    # top left
    row_to_check = cur_col + -1
    col_to_check = cur_row + -1
    if is_index_valid((col_to_check, row_to_check)):
        char = matrix[col_to_check][row_to_check]
        top_left = char
        if char not in count:
            count[char] = 1
        else:
            count[char] += 1

    # top right
    row_to_check = cur_col + 1
    col_to_check = cur_row + -1
    if is_index_valid((col_to_check, row_to_check)):
        char = matrix[col_to_check][row_to_check]
        top_right = char
        if char not in count:
            count[char] = 1
        else:
            count[char] += 1

    # bottom left
    row_to_check = cur_col + -1
    col_to_check = cur_row + 1
    if is_index_valid((col_to_check, row_to_check)):
        char = matrix[col_to_check][row_to_check]
        bottom_left = char
        # print("bottom left : ", char)
        if char not in count:
            count[char] = 1
        else:
            count[char] += 1

    # bottom right
    row_to_check = cur_col + 1
    col_to_check = cur_row + 1
    if is_index_valid((col_to_check, row_to_check)):
        char = matrix[col_to_check][row_to_check]
        bottom_right = char
        # print("bottom right: ", char)
        if char not in count:
            count[char] = 1
        else:
            count[char] += 1

    if ("S" in count and count["S"] == 2) and (
        "M" in count
        and count["M"] == 2
        and (top_left != bottom_right)
        and (top_right != bottom_left)
    ):
        print(index)
        print(count)
        return 1

    return 0


if __name__ == "__main__":
    SAMPLE_INPUT_FILE = "../input/sample.txt"
    MAIN_INPUT_FILE = "../input/main.txt"

    CUR_INPUT = SAMPLE_INPUT_FILE

    temp_list: list[str] = []
    for line in get_data(CUR_INPUT):
        temp_list.append(remove_newline(line))

    DIM = len(get_data(CUR_INPUT))
    matrix = convert_to_2d_matix(temp_list)

    row_count = 0
    col_count = 0
    diag_count = 0

    for i in range(0, DIM):
        for j in range(0, DIM):
            if matrix[i][j] == "A":
                if diagonal_check(matrix, (i, j)):
                    diag_count += 1

    print(f"final ans : {diag_count}")
