# 11559 PuyoPuyo G4

P = [list(input()) for _ in range(12)]


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y) :
    visit[x][y] = 1
    C = P[x][y]
    stack.append((x, y))
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 12 or nx < 0 or ny >= 6 or ny < 0 :
            continue
        if P[nx][ny] != C or visit[nx][ny] :
            continue
        dfs(nx, ny)

def down() :
    for j in range(6) :
        dstack = []
        for i in range(12) :
            if P[i][j] != "." :
                dstack.append(P[i][j])
                P[i][j] = "."
        idx = 11
        while dstack :
            P[idx][j] = dstack.pop()
            idx -=1
    check()

stack = []

def check() :
    global ans, visit
    flag = False
    for i in range(12) :
        for j in range(6) :
            if P[i][j] != '.' :
                stack.clear()
                visit = [[0]*6 for _ in range(12)]
                dfs(i, j)
                if len(stack) >= 4 :
                    while stack :
                        x, y = stack.pop()
                        P[x][y] = '.' 
                    flag = True

    if flag :
        ans += 1
        down()


ans = 0

check()

print(ans)