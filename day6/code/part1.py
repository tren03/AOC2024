# maze puzzle
from enum import Enum


class Direction(Enum):
    UP = "up"
    DOWN = "down"
    LEFT = "left"
    RIGHT = "right"


class Guard:
    position: tuple[int, int]
    direction: Direction
    dimensions: tuple[int, int]
    next_position: tuple[int, int]

    def __init__(
        self,
        initial_pos: tuple[int, int],
        initial_direction: Direction,
        dimensions: tuple[int, int],
    ):
        self.position = initial_pos
        self.direction = initial_direction
        self.dimensions = dimensions

    def up(self):
        self.position = (self.position[0] - 1, self.position[1])

    def down(self):
        self.position = (self.position[0] + 1, self.position[1])

    def left(self):
        self.position = (self.position[0], self.position[1] - 1)

    def right(self):
        self.position = (self.position[0], self.position[1] + 1)

    def get_next_pos(self):
        if self.direction == Direction.UP:
            self.next_position = (self.position[0] - 1, self.position[1])
        if self.direction == Direction.DOWN:
            self.next_position = (self.position[0] + 1, self.position[1])
        if self.direction == Direction.RIGHT:
            self.next_position = (self.position[0], self.position[1] + 1)
        if self.direction == Direction.LEFT:
            self.next_position = (self.position[0], self.position[1] - 1)

    def ahead(self):
        """
        moves ahead one position based on the direction and position
        """
        if self.direction == Direction.UP:
            self.up()
        if self.direction == Direction.DOWN:
            self.down()
        if self.direction == Direction.RIGHT:
            self.right()
        if self.direction == Direction.LEFT:
            self.left()

    def back(self):
        """
        moves back one position based on the direction and position
        """
        if self.direction == Direction.DOWN:
            self.up()
        if self.direction == Direction.UP:
            self.down()
        if self.direction == Direction.LEFT:
            self.right()
        if self.direction == Direction.RIGHT:
            self.left()

    def rotate(self):
        """
        rotates the position of guard by 90 when he reaches a obstacles
        """
        if self.direction == Direction.UP:
            self.direction = Direction.RIGHT
            return

        if self.direction == Direction.RIGHT:
            self.direction = Direction.DOWN
            return

        if self.direction == Direction.DOWN:
            self.direction = Direction.LEFT
            return

        if self.direction == Direction.LEFT:
            self.direction = Direction.UP
            return


def isValid(row: int, col: int, dim: int) -> bool:
    """
    checks if position is valid
    """
    max_row = dim
    max_col = dim

    cur_row = row
    cur_col = col

    if cur_row < 0 or cur_row >= max_row:
        return False
    if cur_col < 0 or cur_col >= max_col:
        return False

    return True


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


def convert_to_2d_matix(str_list: list[str], dim: int) -> list[list[str]]:
    """
    Takes a list[str] and converts in into a 2d matrix where
    each element is a char
    """
    row = 0
    col = 0
    matrix = [[""] * dim for i in range(dim)]
    # print(matrix)
    for line in str_list:
        col = 0
        for char in line:
            matrix[row][col] = char
            col += 1
        row += 1

    return matrix


def simulation(g: Guard, map: list[list[str]]) -> int:
    # just keep calling ahead until we get invalid index
    visited = set()
    while True:
        g.get_next_pos()
        if not isValid(g.position[0], g.position[1], len(map)):
            break

        if isValid(g.next_position[0], g.next_position[1], len(map)):
            if map[g.next_position[0]][g.next_position[1]] == "#":
                g.rotate()

        visited.add(g.position)
        g.ahead()

    return len(visited)


def main():
    SAMPLE_INPUT_FILE = "../input/sample.txt"
    MAIN_INPUT_FILE = "../input/main.txt"

    CUR_INPUT = MAIN_INPUT_FILE

    temp_list: list[str] = []
    for line in get_data(CUR_INPUT):
        temp_list.append(remove_newline(line))

    dim = len(temp_list)
    print(f"dimentsions : {dim}")
    matrix = convert_to_2d_matix(temp_list, dim)
    # print(matrix)

    g = None
    for i in range(0, dim):
        for j in range(0, dim):
            if matrix[i][j] == "^":
                g = Guard((i, j), Direction.UP, (dim, dim))
                break

    if not g:
        print("carrot not found")
    else:
        print(simulation(g, matrix))


if __name__ == "__main__":
    main()
