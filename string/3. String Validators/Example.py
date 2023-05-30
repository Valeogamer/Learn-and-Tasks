if __name__ == '__main__':
    s = input()
    word_isalnum = [letter for letter in s if letter.isalnum()]
    print("".join(word_isalnum).isalnum())
    word_isalpha = [letter for letter in s if letter.isalpha()]
    print("".join(word_isalpha).isalpha())
    word_isdigit = [letter for letter in s if letter.isdigit()]
    print("".join(word_isdigit).isdigit())
    word_islower = [letter for letter in s if letter.islower()]
    print("".join(word_islower).islower())
    word_isupper = [letter for letter in s if letter.isupper()]
    print("".join(word_isupper).isupper())

    # print(s.isalnum())  # check являются ли все символы строки буквенно-цифровыми (az, AZ и 0-9) .
    # print(s.isalpha())  # check являются ли все символы строки алфавитными (az и AZ)
    # print(s.isdigit())  # check являются ли все символы строки цифрами (0-9) .
    # print(s.islower())  # все ли символы строки являются символами нижнего регистра (az) .
    # print(s.isupper())  # все ли символы строки являются символами верхнего регистра (AZ) .
