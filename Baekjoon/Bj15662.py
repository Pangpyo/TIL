# 15662 톱니바퀴(2) G5

import sys


input = sys.stdin.readline

T = int(input())

gears = [input().rstrip() for _ in range(T)]

K = int(input())

R = [0] * T


def teeth(n):
    if n >= 8 or n <= -8:
        return n % 8
    else:
        return n


def rotate(n, c, d):
    if n + 1 < T:
        if d == -1:
            pass
        elif gears[n][teeth(2 - R[n])] != gears[n + 1][teeth(6 - R[n + 1])]:
            rotate(n + 1, -c, 1)
    if n - 1 >= 0:
        if d == 1:
            pass
        elif gears[n][teeth(6 - R[n])] != gears[n - 1][teeth(2 - R[n - 1])]:
            rotate(n - 1, -c, -1)
    R[n] = teeth(R[n] + c)


for _ in range(K):
    n, c = map(int, input().split())
    rotate(n - 1, c, 0)

ans = 0
for i in range(T):
    if gears[i][-R[i]] == "1":
        ans += 1

print(ans)
