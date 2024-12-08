import logging
import re

logger = logging.getLogger(__name__)


def log_config(debug: bool):
    if debug:
        logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")
    else:
        logging.basicConfig(level=logging.CRITICAL)


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


def validator(
    list_to_check: list[int], nos: int, before_list: list[int], after_list: list[int]
) -> bool:
    res = True
    before_to_check: list[int] = []
    after_to_check: list[int] = []
    flag_check: bool = (
        False  # if we reach element, make flag true to add ele to after_to_check list
    )
    for i in list_to_check:
        if i == nos:
            flag_check = True
            continue
        elif flag_check:
            after_to_check.append(i)
        else:
            before_to_check.append(i)

    logger.info(f"nos to check : {nos}")
    logger.info(f"before list to check : {before_to_check}")
    logger.info(f"after list to check  : {after_to_check}")

    # in before_to_check, if there are any elements that should come after i.e in the after_list, then return false
    for i in before_to_check:
        for j in before_list:
            if i == j:
                return False

    # in after_to_check, if there are any elements that should come before i.e in the before_list, then return false
    for i in after_to_check:
        for j in after_list:
            if i == j:
                return False

    return True


def get_middle_ele(l: list[int]) -> int:
    middle_index = len(l) // 2
    return l[middle_index]


if __name__ == "__main__":
    SAMPLE_INPUT_FILE = "../input/sample.txt"
    MAIN_INPUT_FILE = "../input/main.txt"

    DEBUG_MODE = True
    CUR_INPUT = MAIN_INPUT_FILE

    # log_config(DEBUG_MODE)
    # logger.info(get_data(CUR_INPUT))
    logging.basicConfig(level=logging.CRITICAL, format="%(levelname)s: %(message)s")

    clean_data = []
    for line in get_data(CUR_INPUT):
        clean_data.append(remove_newline(line))

    logger.info(f"clean data = {clean_data}\n")

    limits = []
    records = []
    flag = False  # determines where we should input data in records
    for obj in clean_data:
        if obj == "":
            flag = True
        elif flag:
            records.append(obj)
        else:
            limits.append(obj)
    logger.info(limits)
    logger.info("\n")

    record_list: list[list[int]] = []
    for line in records:
        temp = re.findall(r"\d+", line)
        t_nos = []
        for t in temp:
            t_nos.append(int(t))
        record_list.append(t_nos)

    logger.info(f"records : {record_list}")

    # result  is a list of lists, where each list containes two numbers present in each line
    result = []
    for obj in limits:
        temp = re.findall(r"\d+", obj)
        t_nos = []
        for t in temp:
            t_nos.append(int(t))
        result.append(t_nos)

    # Read it as the key should come before all the values in the list its pointing too
    before = {}
    for ele in result:
        if ele[0] not in before:
            before[ele[0]] = [ele[1]]
        else:
            before[ele[0]].append(ele[1])

    logger.info(f"before : {before}")

    # Read it as the key should come after all the values in the list its pointing too
    after = {}
    for ele in result:
        if ele[1] not in after:
            after[ele[1]] = [ele[0]]
        else:
            after[ele[1]].append(ele[1])

    logger.info(f"after : {after}")

    # logger.info(validator(record_list[0], 75, before[75], after[75]))
    # logger.info(validator(record_list[3], 75, before[75], after[75]))

    ans = 0
    for line in record_list:
        flag = True  # assume line is valid record
        for nos_to_check in line:

            if nos_to_check not in before:
                b_list = []
            else:
                b_list = before[nos_to_check]
            if nos_to_check not in after:
                a_list = []
            else:
                a_list = after[nos_to_check]

            if not validator(line, nos_to_check, b_list, a_list):
                flag = False
                break
        if flag == False:
            logger.warning(f"line [{line}] is not valid")
        else:
            ans += get_middle_ele(line)

    print(f"answer = {ans}")

    # logger.info(result)
    # Example logs
    # logger.debug("This is a debug log.")
    # logger.info("This is an info log.")
    # logger.warning("This is a warning log.")
    # logger.error("This is an error log.")
    # logger.critical("This is a critical log.")
