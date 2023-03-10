# 1103 게임 G2
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N, M = map(int, input().split())

B = [list(input().rstrip()) for _ in range(N)]


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
ans = 0

visit = [[0] * M for _ in range(N)]


def dfs(x, y, v):
    l = int(B[x][y])
    n = x * M + y
    v = v | 1 << n
    if not visit[x][y]:
        visit[x][y] = 1
        for i in range(4):
            nx = x + dx[i] * l
            ny = y + dy[i] * l
            if nx >= N or nx < 0 or ny >= M or ny < 0:
                continue
            if B[nx][ny] == "H":
                continue
            nn = nx * M + ny
            if v & 1 << nn:
                print(-1)
                exit()
            visit[x][y] = max(dfs(nx, ny, v | 1 << nn) + 1, visit[x][y])
    return visit[x][y]


print(dfs(0, 0, 0))
