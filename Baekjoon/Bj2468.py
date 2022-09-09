# 2468 안전 영역 S1


import sys

sys.stdin = open('input.txt')
sys.setrecursionlimit(10**6)
input =  sys.stdin.readline
N = int(input())

area = [list(map(int, input().split())) for _ in range(N)]
top = max(map(max, area))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y, n) :
    if area[x][y] > n :
        visit[x][y] = 1
    else :
        return
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= N or nx < 0 or ny >= N or ny < 0 :
            continue
        if visit[nx][ny] :
            continue
        if area[nx][ny] > n:
            dfs(nx, ny, n)
ans = 0
for n in range(top) :
    cnt = 0
    visit = [[0]*N for _ in range(N)]
    for i in range(N) :
        for j in range(N) :
            if not visit[i][j] and area[i][j] > n:
                dfs(i, j, n)
                cnt += 1
    ans = cnt if cnt > ans else ans
print(ans)