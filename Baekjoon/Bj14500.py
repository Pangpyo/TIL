# 14500 테트로미노 G4

N, M = map(int, input().split())

B = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def dfs(x, y):
    stack = [(x, y, [(x, y)])]
    ans = 0
    while stack:
        x, y, v = stack.pop()
        if len(v) == 4:
            temp = sum([B[x][y] for x, y in v])
            ans = max(ans, temp)
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= N or nx < 0 or ny >= M or ny < 0:
                continue
            if (nx, ny) in v:
                continue
            stack.append((nx, ny, v + [(nx, ny)]))
    return ans


def bfs(x, y):
    mid = B[x][y]
    nv = [0, 0, 0, 0]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= N or nx < 0 or ny >= M or ny < 0:
            continue
        nv[i] = B[nx][ny]
    ans = 0
    for i in range(4):
        temp = mid
        flag = True
        for j in range(4):
            if i == j:
                continue
            if nv[j]:
                temp += nv[j]
            else:
                flag = False
                break
        if flag:
            ans = max(temp, ans)
    return ans


visit = [[0] * M for _ in range(N)]


answer = 0
for i in range(N):
    for j in range(M):
        answer = max(dfs(i, j), bfs(i, j), answer)

print(answer)
