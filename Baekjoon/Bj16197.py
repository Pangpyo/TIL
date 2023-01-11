# 16197 두 동전 G4

from collections import deque
import sys

input = sys.stdin.readline


n, m = map(int, input().split())

T = []
C = []
que = deque()
for i in range(n):
    t = input()
    T.append(t)
    for j in range(m):
        if t[j] == "o":
            C.append(i)
            C.append(j)
C.append(0)
que.append(C)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

visit = {}


def answer():
    while que:
        x1, y1, x2, y2, d = que.popleft()
        for i in range(4):
            nx1 = x1 + dx[i]
            ny1 = y1 + dy[i]
            nx2 = x2 + dx[i]
            ny2 = y2 + dy[i]
            out = 0
            b = 0
            if (nx1, ny1, nx2, ny2) in visit:
                continue
            if nx1 >= n or nx1 < 0 or ny1 >= m or ny1 < 0:
                out += 1
            if nx2 >= n or nx2 < 0 or ny2 >= m or ny2 < 0:
                out += 1
            if out == 2:
                continue
            elif out == 1:
                return d + 1
            if d == 9:
                continue
            if T[nx1][ny1] == "#":
                nx1 = x1
                ny1 = y1
                b += 1
            if T[nx2][ny2] == "#":
                nx2 = x2
                ny2 = y2
                b += 1
            if b == 2:
                continue
            if nx1 == nx2 and ny1 == ny2:
                continue
            visit[(nx1, ny1, nx2, ny2)] = 1
            que.append((nx1, ny1, nx2, ny2, d + 1))
    return -1


print(answer())
