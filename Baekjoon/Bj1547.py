# 1547 공 B3

import sys


sys.stdin = open('input.txt')

M = int(input())

cups = [1, 0, 0]

for i in range(M) :
    x, y = map(int, input().split())
    cupx = cups[x-1]
    cupy = cups[y-1]
    cups[x-1] = cupy
    cups[y-1] = cupx
print(cups.index(1)+1)
