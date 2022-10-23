# 11660 구간 합 구하기5 S1


import sys

# input = sys.stdin.readline
sys.stdin = open("input.txt")

N, M = map(int, input().split())

table = [list(map(int, input().split())) for _ in range(N)]


for i in range(N):
    for j in range(1, N):
        table[i][j] += table[i][j - 1]

for i in range(1, N):
    for j in range(N):
        table[i][j] += table[i - 1][j]

for i in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    xsum = 0
    ysum = 0
    xysum = 0
    if x1 > 1:
        ysum = table[x1 - 2][y2 - 1]
    if y1 > 1:
        xsum = table[x2 - 1][y1 - 2]
    if x1 > 1 and y1 > 1:
        xysum = table[x1 - 2][y1 - 2]
    ans = table[x2 - 1][y2 - 1] - xsum - ysum + xysum
    print(ans)
