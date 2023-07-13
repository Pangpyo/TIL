# 1577 도로의 개수 G5

import sys


def solution() :
    input = sys.stdin.readline
    N, M = map(int, input().split())
    
    weak = [[set() for _ in range(M+1)] for _ in range(N+1)]
    
    K = int(input())
    dx = [1, 0]
    dy = [0, 1]
    for _ in range(K) :
        a, b, c, d = map(int, input().split())
        weak[a][b].add((c, d))
        weak[c][d].add((a, b))
    visit = [[0]*(M+1) for _ in range(N+1)]
    visit[N][M] = 1
    def dfs(x, y) :
        if visit[x][y] :
            return visit[x][y]
        temp = 0
        for i in range(2) :
            nx = x + dx[i]
            ny = y + dy[i]
            if nx > N or ny > M : 
                continue
            if (nx, ny) in weak[x][y] :
                continue

            temp += dfs(nx, ny)
            
        visit[x][y] = temp
        return temp
    
    ans = dfs(0, 0)
    return ans

if __name__ == "__main__" :
    print(solution())  