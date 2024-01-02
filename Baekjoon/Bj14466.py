# 소가 길을 건너간 이유 6 G4

import sys


def solution() :
    input = sys.stdin.readline
    N, K, R = map(int, input().split())
    map_ = [[0]*N for _ in range(N)]

    dx = (-1, 0, 1, 0)
    dy = (0, 1, 0, -1)


    for _ in range(R) :
        r, c, r_, c_ = map(lambda x : int(x)-1, input().split())
        if r - r_ == -1 :
            map_[r][c] |= (1<<2)
            map_[r_][c_] |= (1<<0)
        elif r - r_ == 1 :
            map_[r][c] |= (1<<0)
            map_[r_][c_] |= (1<<2)
        elif c - c_  == -1 :
            map_[r][c] |= (1<<1)
            map_[r_][c_] |= (1<<3)
        else :
            map_[r][c] |= (1<<3)
            map_[r_][c_] |= (1<<1)
    
    cow_map = [[-1]*N for _ in range(N)]
    cows = []
    for i in range(K) :
        x, y = map(lambda x : int(x)-1, input().split())
        cows.append((x, y))
        cow_map[x][y] = i

    def dfs(x, y, n) :
        visit[x][y] = 1
        for i in range(4) :
            if map_[x][y] & (1<<i) :
                continue
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= N or nx < 0 or ny >= N or ny < 0 :
                continue
            if visit[nx][ny] :
                continue
            if cow_map[nx][ny] != -1 :
                meet[n][cow_map[nx][ny]] = 1
            dfs(nx, ny, n)

    meet = [[0]*K for _ in range(K)]
    for i in range(K) :
        visit = [[0]*N for _ in range(N)]
        x, y = cows[i]
        dfs(x, y, i)
    answer = 0
    for i in range(K) :
        cnt = K - 1 - i
        for j in range(i+1, K) :
            if meet[i][j] :
                cnt -= 1
        answer += cnt
    return answer

if __name__ == "__main__" :
    print(solution())