# 2295 세 수의 합 G4

import sys

input = sys.stdin.readline

N = int(input())

U = sorted([int(input()) for _ in range(N)])

setU = set()

for x in U:
    for y in U:
        setU.add(x + y)


def answer():
    for i in reversed(range(N)):
        for j in range(i + 1):
            if U[i] - U[j] in setU:
                return U[i]


print(answer())
