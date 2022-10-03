# 9465 스티커 S1

import sys

input = sys.stdin.readline

for t in range(int(input())):
    n = int(input())

    stikers = [list(map(int, input().split())) for _ in range(2)]

    if n == 1:
        print(max(stikers[0][0], stikers[1][0]))
    elif n == 2:
        print(max(stikers[0][0] + stikers[1][1], stikers[1][0] + stikers[0][1]))
    else:
        D = [
            [stikers[0][0], stikers[1][0] + stikers[0][1]],
            [stikers[1][0], stikers[0][0] + stikers[1][1]],
        ]
        for i in range(2, n):
            D[0].append(max(D[1][i - 1], D[1][i - 2]) + stikers[0][i])
            D[1].append(max(D[0][i - 1], D[0][i - 2]) + stikers[1][i])
        print(max(D[0][n - 1], D[1][n - 1]))
