def build_prefix_table(pattern):
    prefix_table = [0] * len(pattern)
    j = 0
    for i in range(1, len(pattern)):
        if pattern[i] == pattern[j]:
            j += 1
            prefix_table[i] = j
        else:
            if j != 0:
                j = prefix_table[j - 1]
                i -= 1
            else:
                prefix_table[i] = 0
    return prefix_table

def kmp_search(text, pattern):
    prefix_table = build_prefix_table(pattern)
    i = j = 0
    while i < len(text) and j < len(pattern):
        if text[i] == pattern[j]:
            i += 1
            j += 1
        else:
            if j != 0:
                j = prefix_table[j - 1]
            else:
                i += 1
    if j == len(pattern):
        return i - j
    return -1

# Пример использования
text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"

result = kmp_search(text, pattern)

if result != -1:
    print("Подстрока найдена в позиции", result)
else:
    print("Подстрока не найдена")
