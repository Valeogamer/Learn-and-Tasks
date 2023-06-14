import math
languages = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
num = int(input())
cnt = math.ceil(len(languages) / num)
cnt_b = 0
cnt_e = num
s = ""
for i in range(cnt):
    s += languages[cnt_b:cnt_e] + "\n"
    cnt_b += num
    cnt_e += num
print(s)
