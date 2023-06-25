# 28256 초콜릿 보관함

def solution() :
    board = [list(input()) for _ in range(3)]
    S = list(map(int, input().split()))
    n = S[0]
    nums = S[1::]
    visit = [[0]*3 for _ in range(3)]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    def dfs(x, y) :
        visit[x][y] = 1
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 3 or nx < 0 or ny >= 3 or ny < 0 :
                continue
            if board[nx][ny] != "O" or visit[nx][ny] :
                continue
            visit[x][y] += dfs(nx, ny)
        return visit[x][y]
    ans = []
    for i in range(3) :
        for j in range(3) :
            if visit[i][j] or board[i][j] != "O" :
                continue
            ans.append(dfs(i, j))
    ans.sort()
    return int(nums == ans)

if __name__ == "__main__" :
    for _ in range(int(input())) :
        print(solution())
