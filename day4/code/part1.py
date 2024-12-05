"""
top -1,0
bottom  1,0

left 0,-1
right 0,1

top left  -1,-1
top right -1,1

bottom left 1,-1
bottom right  1,1
"""


# Takes a string and removes newline at the end of the string
def remove_newline(string: str) -> str:
    mod_string = string.removesuffix("\n")
    return mod_string


# Gets the data from the file
def get_data(filepath: str) -> list[str]:
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
    if index[0] < DIM and index[0] >= 0 and index[1] < DIM and index[1] >= 0:
        return True
    return False


def col_check(matrix: list[list[str]], index: tuple[int, int]) -> int:
    """
    we get the matrix and index of x to process if xmas exists in col, we update the row here
    """
    count = 0
    front_check = [0, 1, 2, 3]
    back_check = [0, -1, -2, -3]
    cur_row = index[0]
    cur_col = index[1]
    final_front_string: str = ""
    final_back_string: str = ""

    for i in front_check:
        row_to_check = cur_row + i
        if is_index_valid((row_to_check, cur_col)):
            final_front_string += matrix[row_to_check][cur_col]

    for i in back_check:
        row_to_check = cur_row + i
        if is_index_valid((row_to_check, cur_col)):
            final_back_string += matrix[row_to_check][cur_col]

    if final_front_string == "XMAS":
        count += 1

    if final_back_string == "XMAS":
        count += 1

    return count


def row_check(matrix: list[list[str]], index: tuple[int, int]) -> int:
    """
    we get the matrix and index of x to process if xmas exists in row, we update the column here
    """
    count = 0
    front_check = [0, 1, 2, 3]
    back_check = [0, -1, -2, -3]
    cur_row = index[0]
    cur_col = index[1]
    final_front_string: str = ""
    final_back_string: str = ""
    for i in front_check:
        col_to_check = cur_col + i
        if is_index_valid((cur_row, col_to_check)):
            final_front_string += matrix[cur_row][col_to_check]

    for i in back_check:
        col_to_check = cur_col + i
        if is_index_valid((cur_row, col_to_check)):
            final_back_string += matrix[cur_row][col_to_check]

    if final_front_string == "XMAS":
        count += 1

    if final_back_string == "XMAS":
        count += 1

    return count


def diagonal_check(matrix: list[list[str]], index: tuple[int, int]) -> int:
    """
    we get the matrix and index of x to process if xmas exists in diagonal, we update the row,column here
    """
    count = 0
    pos_check = [0, 1, 2, 3]
    neg_check = [0, -1, -2, -3]
    cur_row = index[0]
    cur_col = index[1]

    top_left = ""
    top_right = ""
    bottom_left = ""
    bottom_right = ""

    # top left
    for i in range(0, 4):
        row_to_check = cur_col + neg_check[i]
        col_to_check = cur_row + neg_check[i]
        if is_index_valid((row_to_check, col_to_check)):
            top_left += matrix[row_to_check][col_to_check]

    # top right
    for i in range(0, 4):
        row_to_check = cur_col + pos_check[i]
        col_to_check = cur_row + neg_check[i]
        if is_index_valid((row_to_check, col_to_check)):
            top_right += matrix[row_to_check][col_to_check]

    # bottom left
    for i in range(0, 4):
        row_to_check = cur_col + neg_check[i]
        col_to_check = cur_row + pos_check[i]
        if is_index_valid((row_to_check, col_to_check)):
            bottom_left += matrix[row_to_check][col_to_check]

    # bottom right
    for i in range(0, 4):
        row_to_check = cur_col + pos_check[i]
        col_to_check = cur_row + pos_check[i]
        if is_index_valid((row_to_check, col_to_check)):
            bottom_right += matrix[row_to_check][col_to_check]

    if top_left == "XMAS":
        count += 1

    if top_right == "XMAS":
        count += 1

    if bottom_left == "XMAS":
        count += 1

    if bottom_right == "XMAS":
        count += 1

    return count


if __name__ == "__main__":
    SAMPLE_INPUT_FILE = "../input/sample.txt"
    MAIN_INPUT_FILE = "../input/main.txt"

    CUR_INPUT = MAIN_INPUT_FILE

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
            if row_check(matrix, (i, j)):
                row_count += row_check(matrix, (i, j))
            if col_check(matrix, (i, j)):
                col_count += col_check(matrix, (i, j))
            if diagonal_check(matrix, (i, j)):
                diag_count += diagonal_check(matrix, (i, j))

    print(row_count)
    print(col_count)
    print(diag_count)
    print(f"final ans : {row_count+col_count+diag_count}")
