from itertools import permutations


def func_permutations(words):
    word = ''
    for letter in words[:-1]:
        word += letter
    n = words[-1]
    per = list(permutations(str(word), int(n)))
    per.sort()
    sum_word = ''
    for subword in per:
        letters = ''
        for letter in subword:
            letters += letter
        sum_word += letters + '\n'
    return sum_word


if __name__ == '__main__':
    words = [i for i in str(input()) if i != ' ']
    print(func_permutations(words))
