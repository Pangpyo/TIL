# 6593 상범빌딩 G5


from collections import deque
import sys

input = sys.stdin.readline
while 1:
    L, R, C = map(int, input().split())

    if L == R == C == 0:
        break

    building = []
    start = ()
    for i in range(L):
        room = []
        for j in range(R):
            temp = list(input())
            room.append(temp)
            for k in range(C):
                if temp[k] == "S":
                    start = (i, j, k)
        input()
        building.append(room)

    def bfs(x, y, z):
        visit = [[[0] * C for _ in range(R)] for _ in range(L)]
        dx = [-1, 1, 0, 0, 0, 0]  # 상 하 좌 우 전 후
        dy = [0, 0, -1, 1, 0, 0]
        dz = [0, 0, 0, 0, -1, 1]
        que = deque()
        que.append((x, y, z, 0))
        visit[x][y][z] == 1
        while que:
            x, y, z, t = que.popleft()
            for i in range(6):
                nx = x + dx[i]
                ny = y + dy[i]
                nz = z + dz[i]
                if nx >= L or nx < 0 or ny >= R or ny < 0 or nz >= C or nz < 0:
                    continue
                if visit[nx][ny][nz]:
                    continue
                if building[nx][ny][nz] == "#":
                    continue
                if building[nx][ny][nz] == "E":
                    print(f"Escaped in {t+1} minute(s).")
                    return
                que.append((nx, ny, nz, t + 1))
                visit[nx][ny][nz] = 1
        print("Trapped!")
        return

    bfs(*start)
