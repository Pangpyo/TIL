# 15683 감시 G4

N, M = map(int, input().split())

room = []
empty = N * M
cctv = []
for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(M):
        if temp[j]:
            if temp[j] != 6:
                cctv.append((temp[j] - 1, i, j))
            empty -= 1
    room.append(temp)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

see = [[0], [0, 2], [0, 1], [0, 1, 2], [0, 1, 2, 3]]

l = len(cctv)
ans = 0


dc = [4, 2, 4, 4, 1]
stack = []


def dfs(cnt, s):
    global room, ans
    if cnt == l:
        ans = max(ans, s)
        return
    dr, x, y = cctv[cnt]
    for i in range(dc[dr]):
        temp = 0
        for d in see[dr]:
            nx = x
            ny = y
            while 1:
                di = (d + i) % 4
                nx = nx + dx[di]
                ny = ny + dy[di]
                if nx >= N or nx < 0 or ny >= M or ny < 0:
                    break
                if room[nx][ny] == 6:
                    break
                if not room[nx][ny]:
                    room[nx][ny] = -1
                    temp += 1
                    stack.append((nx, ny))
        dfs(cnt + 1, s + temp)
        for t in range(temp):
            ex, ey = stack.pop()
            room[ex][ey] = 0


dfs(0, 0)
print(empty - ans)
