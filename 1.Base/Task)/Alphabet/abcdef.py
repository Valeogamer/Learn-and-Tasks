import string

ALPHABET = string.ascii_lowercase


def alphab_ascii(num) -> str:
    """
    with ASCII
    :param num: count uni letter
    :return: result
    """
    current_letter: list[str] = [letter for letter in ALPHABET[:num]]
    old_letter: str = ''
    len_long_line: int = 4 * num - 3
    result: list[str] = []
    list_left: list[str] = []
    for i in reversed(current_letter):
        old_letter += f'{i}'
        list_left.append('-'.join(old_letter).rjust(int(len_long_line / 2) + 1, '-'))
    new_mat = list_left[:-1]
    for i in reversed(new_mat):
        list_left.append(i)
    list_right_old = [sublist[::-1] for sublist in list_left]
    list_right = [i[1:] for i in list_right_old]
    for beginning, continuation in zip(list_left, list_right):
        result.append(beginning + continuation)
    result_line: str = ''
    for i in result:
        result_line += f'{i}\n'
    print(result_line)


def alphab(num) -> str:
    """
    non ASCII
    """
    a: int = 97  # число для возврата символа по его числовому значению с помощью метода chr
    current_letter = a + num - 1
    old_state = ''
    len_long_line = 4 * num - 3
    result = []
    list_left = []
    for i in range(current_letter, a - 1, -1):
        # print(chr(i).center(long_line, '-'))
        old_state += f'{chr(i)}'
        list_left.append('-'.join(old_state).rjust(int(len_long_line / 2) + 1, '-'))
    new_mat = list_left[:-1]
    for i in reversed(new_mat):
        list_left.append(i)
    list_right_old = [sublist[::-1] for sublist in list_left]
    list_right = [i[1:] for i in list_right_old]
    for beginning, continuation in zip(list_left, list_right):
        result.append(beginning + continuation)
    result_line = ''
    for i in result:
        result_line += f'{i}\n'
    print(result_line)


if __name__ == '__main__':
    num = int(input())
    alphab_ascii(n)
