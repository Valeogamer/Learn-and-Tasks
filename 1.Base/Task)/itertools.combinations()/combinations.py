from itertools import combinations


def func_combinations(words):
    word = ''
    sort_word = words[:-1]
    sort_word.sort()
    for i in sort_word:
        word += i
    sort_letter =''
    for i in sort_word:
        sort_letter += i + '\n'
    n = words[-1]
    per = list(combinations(str(word), int(n)))
    per.sort()
    sum_word = ''
    for subword in per:
        letters = ''
        for letter in subword:
            letters += letter
        sum_word += letters + '\n'
    return sort_letter + sum_word


if __name__ == '__main__':
    words = [i for i in str(input()) if i != ' ']
    print(func_combinations(words))
