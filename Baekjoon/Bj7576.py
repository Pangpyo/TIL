# 7576 토마토 G5

from collections import deque
import sys


input = sys.stdin.readline

M, N = map(int, input().split())

tomatos = [list(map(int, input().split())) for _ in range(N)]
ripe = deque() # 일반적인 list에서 pop(0)을 했을 때 시간초과가 났다. deque의 중요성을 깨달았다.
for i in range(N) :
    for j in range(M) :
        if tomatos[i][j] == 1 :
            ripe.append((i, j, 0))
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
ans = 0
while ripe :
    x, y, d = ripe.popleft()
    ans = d if d > ans else ans
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= N or nx < 0 or ny >= M or ny < 0 :
            continue
        if tomatos[nx][ny] == 0 :
            tomatos[nx][ny] = 1
            ripe.append((nx, ny, d+1))
for i in tomatos :
    if 0 in i :
        ans = -1
        break
print(ans)

