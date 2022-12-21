# 3055 탈출 G4


from collections import deque

R, C = map(int, input().split())

forest = [list(input()) for _ in range(R)]

waters = []

S = ()

for i in range(R):
    for j in range(C):
        if forest[i][j] == "S":
            S = (i, j)
        elif forest[i][j] == "*":
            waters.append((i, j))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def expand():
    global waters
    nwaters = []
    for x, y in waters:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= R or nx < 0 or ny >= C or ny < 0:
                continue
            if forest[nx][ny] == ".":
                forest[nx][ny] = "*"
                nwaters.append((nx, ny))
    waters = nwaters


visit = [[0] * C for _ in range(R)]


def bfs(x, y):
    que = deque()
    que.append((x, y, 0))
    time = 0
    j = 0
    expand()
    while que:
        x, y, t = que.popleft()
        if t > time:
            expand()
            time += 1
        j += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= R or nx < 0 or ny >= C or ny < 0 or visit[nx][ny]:
                continue
            if forest[nx][ny] == "D":
                return t + 1
            elif forest[nx][ny] == ".":
                visit[nx][ny] = 1
                que.append((nx, ny, t + 1))

    return "KAKTUS"


print(bfs(*S))
