# 16932 모양 만들기 G3

import sys


input = sys.stdin.readline

N, M = map(int, input().split())

nums = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def dfs(x, y):
    global cnt
    stack = [(x, y)]
    nums[x][y] = cnt
    size = 1
    while stack:
        x, y = stack.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= N or nx < 0 or ny >= M or ny < 0:
                continue
            if nums[nx][ny] == 1:
                nums[nx][ny] = cnt
                size += 1
                stack.append((nx, ny))
    sizes.append(size)


cnt = 2
sizes = []

for i in range(N):
    for j in range(M):
        if nums[i][j] == 1:
            dfs(i, j)
            cnt += 1

ans = 0
for x in range(N):
    for y in range(M):
        if not nums[x][y]:
            temp = set()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx >= N or nx < 0 or ny >= M or ny < 0:
                    continue
                if nums[nx][ny]:
                    temp.add(nums[nx][ny] - 2)
            ans = max(ans, sum([sizes[i] for i in temp]) + 1)

print(ans)
