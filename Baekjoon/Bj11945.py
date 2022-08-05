# 11945 뜨거운 붕어빵 B4

import sys


sys.stdin = open('input.txt')

N, M = map(int, input().split())

print(*[input()[::-1] for _ in range(N)], sep = '\n')
