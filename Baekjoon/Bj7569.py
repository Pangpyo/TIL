# 7569 토마토 G5

from collections import deque
import sys


input = sys.stdin.readline

M, N, H = map(int, input().split())

tomatos = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
ripe = deque() # 일반적인 list에서 pop(0)을 했을 때 시간초과가 났다. deque의 중요성을 깨달았다.
for i in range(N) :
    for j in range(M) :
        for k in range(H) :
            if tomatos[k][i][j] == 1 :
                ripe.append((i, j, k, 0))
dx = [-1, 0, 1, 0, 0, 0]
dy = [0, 1, 0, -1, 0, 0]
dh = [0, 0, 0, 0, -1, 1]
ans = 0
while ripe :
    x, y, h, d = ripe.popleft()
    ans = d if d > ans else ans
    for i in range(6) :
        nx = x + dx[i]
        ny = y + dy[i]
        nh = h + dh[i]
        if nx >= N or nx < 0 or ny >= M or ny < 0 or nh >= H or nh < 0 :
            continue
        if tomatos[nh][nx][ny] == 0 :
            tomatos[nh][nx][ny] = 1
            ripe.append((nx, ny, nh, d+1))
for i in tomatos :
    for j in i :
        if 0 in j :
            ans = -1
            break
print(ans)

