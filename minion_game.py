def minion_game(string):
    vowels = "AEIOU"
    length = len(string)
    stuart_score = 0
    kevin_score = 0
    for i in range(length):
        if string[i] in vowels:
            kevin_score += length - i
        else:
            stuart_score += length - i
    if stuart_score > kevin_score:
        print("Stuart", stuart_score)
    elif kevin_score > stuart_score:
        print("Kevin", kevin_score)
    else:
        print("Draw")


if __name__ == '__main__':
    # s = input("ВВедите : ")
    # minion_game(s)
    s = "BANANA"
    minion_game(s)
