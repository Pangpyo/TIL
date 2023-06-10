# 5913 준규와 사과 G4

def solution() :
    K = int(input())
    A = [[0]*5 for _ in range(5)]
    for _ in range(K) :
        x, y = map(int, input().split())
        A[x-1][y-1] = 1
    l = (25-K)//2 + 1
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    visit = [[0]*5 for _ in range(5)]
    visit[0][0] = 1
    visit[4][4] = 1
    cnt = 0
    def dfs(x, y, d, h) :
        nonlocal cnt
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 5 or nx < 0 or ny >= 5 or ny < 0 :
                continue
            if A[nx][ny] or visit[nx][ny] == 1:
                continue
            if d + 1 == l:
                if not h :
                    visit[nx][ny] = 2
                    dfs(4, 4, 1, True)
                    visit[nx][ny] = 0
                if h and visit[nx][ny] == 2 :
                    cnt += 1
                continue
            if visit[nx][ny] == 2 :
                continue
            visit[nx][ny] = 1
            dfs(nx, ny, d+1, h)
            visit[nx][ny] = 0
    dfs(0, 0, 1, False)

    return cnt

if __name__ == "__main__" :
    print(solution())