# 11123 양 한마리... 양 두마리... S2


import sys

sys.setrecursionlimit(
    10**5
)  # 파이썬의 재귀제한은 1000. 이 문제에서는 그래프의 크기가 최대 10000이므로 제한을 이렇게 설정해준다

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

input = sys.stdin.readline


def dfs(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= H or nx < 0 or ny >= W or ny < 0 or visit[nx][ny]:
            continue
        visit[nx][ny] = 1
        if grid[nx][ny] == "#":
            dfs(nx, ny)


for t in range(int(input())):
    H, W = map(int, input().split())
    grid = tuple(
        input().rstrip() for _ in range(H)
    )  # 인덱스 접근 시간을 최대한 아끼기 위해 이렇게 만들어보았다..
    visit = [[0] * W for _ in range(H)]  # 방문처리
    cnt = 0
    for i in range(H):
        for j in range(W):
            if not visit[i][j] and grid[i][j] == "#":
                visit[i][j] = 1
                dfs(i, j)
                cnt += 1
    print(cnt)
