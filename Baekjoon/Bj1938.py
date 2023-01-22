# 1938 통나무 옮기기 G2

from collections import deque


N = int(input())

g = []
BBB = []
EEE = []
for i in range(N):
    temp = input()
    for j in range(N):
        if temp[j] == "B":
            BBB.append((i, j))
        elif temp[j] == "E":
            EEE.append((i, j))
    g.append(temp)


s = (*BBB[1], 0 if BBB[0][0] == BBB[1][0] else 1)
e = (*EEE[1], 0 if EEE[0][0] == EEE[1][0] else 1)

visit = [[[0, 0] for _ in range(N)] for _ in range(N)]

visit[s[0]][s[1]][s[2]] = 1

que = deque([(*s, 0)])

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

dx8 = [-1, -1, -1, 0, 0, 1, 1, 1]
dy8 = [-1, 0, 1, -1, 1, -1, 0, 1]


def check(x, y):
    if x + 1 >= N or x - 1 < 0 or y + 1 >= N or y - 1 < 0:
        return False
    else:
        for i in range(8):
            nx = x + dx8[i]
            ny = y + dy8[i]
            if g[nx][ny] == "1":
                return False
        return True


def answer():
    while que:
        x, y, d, cnt = que.popleft()
        if not visit[x][y][(d + 1) % 2] and check(x, y):
            if (x, y, (d + 1) % 2) == e:
                return cnt + 1
            que.appendleft((x, y, (d + 1) % 2, cnt + 1))
            visit[x][y][(d + 1) % 2] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= N or nx < 0 or ny >= N or ny < 0 or g[nx][ny] == "1":
                continue
            if d == 0:
                if (
                    ny + 1 >= N
                    or ny - 1 < 0
                    or g[nx][ny - 1] == "1"
                    or g[nx][ny + 1] == "1"
                ):
                    continue
            else:
                if (
                    nx + 1 >= N
                    or nx - 1 < 0
                    or g[nx - 1][ny] == "1"
                    or g[nx + 1][ny] == "1"
                ):
                    continue
            if not visit[nx][ny][d]:
                if (nx, ny, d) == e:
                    return cnt + 1
                que.append((nx, ny, d, cnt + 1))
                visit[nx][ny][d] = 1
    return 0


print(answer())
