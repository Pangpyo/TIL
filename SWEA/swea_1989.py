# 1989. 초심자의 회문 검사 D2

import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for i in range(1, T+1) :
    word = input()
    t = 1 if word == word[::-1] else 0
    print('#%d'%i,t)