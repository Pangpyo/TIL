# 9093 단어 뒤집기 B1

import sys


sys.stdin = open('input.txt')

T = int(input())

for i in range(T) :
    sentence = list(input().split())
    for word in sentence :
        print(word[::-1], end = ' ')
    print()