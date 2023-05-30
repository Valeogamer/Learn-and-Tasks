def swap_case(s: str):
    letter = [leter for leter in s]
    word = []
    for i in letter:
        if i.isupper():
            word.append(i.lower())
        elif i.islower():
            word.append(i.upper())
        else:
            word.append(i)
    words = "".join(word)
    return words


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
