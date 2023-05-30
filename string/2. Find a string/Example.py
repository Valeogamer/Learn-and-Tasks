def count_substring(string, sub_string):
    """
    Подсчет количества пар букв
    :param string: слово
    :param sub_string: пар буква для поиска
    :return: количество встречающихся пар букв
    """
    words = [letter for letter in string]
    chek_letter = [letter for letter in sub_string]
    len_sub_string = len(sub_string)
    cnt_check = 0
    for i in range(len(words)):
        if words[i:(len_sub_string + i)] == chek_letter:
            cnt_check += 1
    return cnt_check


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)

"""
    Example:
    Intput_1: ABABACAB
    Intput_2: AB
    Output: 3
"""