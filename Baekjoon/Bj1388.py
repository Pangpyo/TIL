# 1388 바닥장식 S4

def solution() :
    N, M = map(int, input().split())
    B = [list(input()) for _ in range(N)]
    visit = [[0]*M for _ in range(N)]

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    def dfs(x, y) :
        visit[x][y] = 1
        n = B[x][y]
        for i in range(4) :
            if n == '|' :
                if i%2 :
                    continue
            else :
                if not i%2 :
                    continue
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= N or nx < 0 or ny >= M or ny < 0 :
                continue
            if visit[nx][ny] or B[nx][ny] != n:
                continue
            dfs(nx, ny)
    ans = 0
    for i in range(N) :
        for j in range(M) :
            if not visit[i][j] :
                dfs(i, j)
                ans += 1
    return ans

if __name__ == "__main__" :
    print(solution())