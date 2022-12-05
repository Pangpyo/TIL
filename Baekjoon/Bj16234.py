# 16234 인구이동 G5

from collections import deque


N, L, R = map(int, input().split())

countrys = [list(map(int, input().split())) for _ in range(N)]


def share(x, y):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    que = deque([(x, y)])
    peaple = 0
    stack = [(x, y)]
    visit[x][y] = 1
    peaple += countrys[x][y]
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= N or nx < 0 or ny >= N or ny < 0:
                continue
            if visit[nx][ny]:
                continue
            diff = abs(countrys[x][y] - countrys[nx][ny])
            if L <= diff <= R:
                que.append((nx, ny))
                stack.append((nx, ny))
                peaple += countrys[nx][ny]
                visit[nx][ny] = 1
    afterpeaple = peaple // len(stack)
    for x, y in stack:
        countrys[x][y] = afterpeaple
    if len(stack) > 1:
        return True
    else:
        return False


days = 0
while True:
    visit = [[0] * N for _ in range(N)]
    move = False
    for i in range(N):
        for j in range(N):
            if not visit[i][j]:
                flag = share(i, j)
                if flag:
                    move = True
    if move:
        days += 1
    else:
        break
print(days)
