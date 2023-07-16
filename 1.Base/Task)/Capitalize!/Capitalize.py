def letter_upper(s):
    ss = [letter for letter in s]
    result = ''
    flag = False
    for i in range(len(ss)):
        if i == 0:
            ss[0] = ss[0].upper()
        if flag:
            ss[i] = ss[i].upper()
            flag = False
        if ss[i] == ' ':
            flag = True
        result += ss[i]
    return result


if __name__ == '__main__':
    s = str(input())
    word_up = letter_upper(s)
    print(word_up)
