# 27211 도넛 행성 G5
# B번 도넛 행성


import sys

sys.setrecursionlimit(10**7)  # 재귀 깊이 설정 1000*1000 이상으로 설정해준다

n, m = map(int, input().split())  #

D = [list(map(int, input().split())) for _ in range(n)]


dx = [-1, 0, 1, 0]  # 4방향 탐색
dy = [0, 1, 0, -1]


def dfs(x, y):  # dfs를 해준다
    D[x][y] = 2  # 내가 밟은 땅은 2로 설정해준다
    for i in range(4):
        nx = (x + dx[i]) % n  # 인덱스를 초과할경우를 대비해 나머지를 구해준다
        ny = (y + dy[i]) % m  # 예시 : -1 % n = n-1, n % n = 0
        if not D[nx][ny]:  # 0인경우에만 그래프를 탐색한다.
            dfs(nx, ny)  # dfs로 재탐색


cnt = 0  # 구역의 수
for i in range(n):
    for j in range(m):
        if not D[i][j]:  # 이 조건문에 들어올 때 마다 구역의 수를 세어 줄 수 있다
            dfs(i, j)
            cnt += 1
print(cnt)
