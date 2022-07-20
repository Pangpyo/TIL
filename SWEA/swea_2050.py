# 2050. 알파벳을 숫자로 변환 D1

import sys

sys.stdin = open("input.txt", "r")

T = input()
a = 64
for i in T :

    print(ord(i)-a, end=' ')