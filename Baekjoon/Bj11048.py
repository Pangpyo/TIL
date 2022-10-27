# 11048 이동하기 S2

import sys


input = sys.stdin.readline

N, M = map(int, input().split())

miro = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(M):
        precandy = []
        if i - 1 >= 0:
            precandy.append(miro[i - 1][j])
        if j - 1 >= 0:
            precandy.append(miro[i][j - 1])
        if i - 1 >= 0 and j - 1 >= 0:
            precandy.append(miro[i - 1][j - 1])
        if precandy:
            miro[i][j] += max(precandy)
print(miro[N - 1][M - 1])
