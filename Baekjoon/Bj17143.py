# 17143 낚시왕 G1

from pprint import pprint
import sys


input = sys.stdin.readline

N, M, S = map(int, input().split())

sharks = [()]
sea = [[0] * M for _ in range(N)]
for i in range(1, S + 1):
    r, c, s, d, z = map(int, input().split())
    if d <= 2:
        s = s % (N * 2 - 2)
    else:
        s = s % (M * 2 - 2)
    d -= 1
    sharks.append((s, d, z))
    sea[r - 1][c - 1] = i

ans = 0


def catch(n):
    temp = 0
    for i in range(N):
        if sea[i][n]:
            sea[i][n] = 0
            temp = sharks[sea[i][n] - 1][2]
    return temp


for i in range(M):
    ans += catch(i)

pprint(sea)

print(ans)
