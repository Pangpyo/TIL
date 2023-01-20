# 17070 파이프 옮기기 1 G5

N = int(input())

home = tuple(tuple(map(int, input().split())) for _ in range(N))
dx = [0, 1, 1]
dy = [1, 1, 0]

cnt = 0


def dfs(x, y, d):
    global cnt
    if x == y == N - 1:
        cnt += 1

    if x + 1 < N and y + 1 < N:
        if not home[x + 1][y] and not home[x][y + 1] and not home[x + 1][y + 1]:
            dfs(x + 1, y + 1, 2)

    if (d == 0 or d == 2) and y + 1 < N:
        if not home[x][y + 1]:
            dfs(x, y + 1, 0)

    if (d == 1 or d == 2) and x + 1 < N:
        if not home[x + 1][y]:
            dfs(x + 1, y, 1)


dfs(0, 1, 0)

print(cnt)
