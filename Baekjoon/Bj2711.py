# 2711 오타맨 고창영 B2

import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for i in range(1, T+1) :
    n, word = input().split()
    n = int(n)-1
    word = word[:n] + word[n+1:]
    print(word)