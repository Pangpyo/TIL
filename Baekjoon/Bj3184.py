# 3184 양 S1

import sys

# 그래프 탐색, 플러드 필
input = sys.stdin.readline
sys.setrecursionlimit(10**6)  # 재귀제한 방지
N, M = map(int, input().split())

field = [list(input()) for _ in range(N)]

O = 0
V = 0

visit = [[0] * M for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def dfs(x, y):  # dfs를 하며 세어준다
    global o, v  # 글로벌로 o, v를 세어줌
    visit[x][y] = 1
    if field[x][y] == "o":
        o += 1
    elif field[x][y] == "v":
        v += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= N or nx < 0 or ny >= M or ny < 0 or visit[nx][ny]:
            continue
        if field[nx][ny] == "#":
            continue
        dfs(nx, ny)


for i in range(N):
    for j in range(M):
        if not visit[i][j] and field[i][j] != "#":
            o, v = 0, 0
            dfs(i, j)
            if o > v:  # 양이 더 많으면 전체 양만 +
                O += o
            else:  # 같거나 적으면 전체 늑대만 +
                V += v

print(O, V)
