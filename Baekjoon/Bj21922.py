# 21922 학부 연구생 민상 G5

import sys

def solution() :
    input = sys.stdin.readline
    N, M = map(int, input().split())
    room = []
    starts = []
    for i in range(N) :
        temp = tuple(map(int, input().split()))
        for j in range(M) :
            if temp[j] == 9 :
                starts.append((i, j))
        room.append(temp)    
    dx = (-1, 0 ,1, 0)
    dy = (0, 1, 0 ,-1)
    visit = [[[0]*4 for _ in range(M)]for _ in range(N)]
    
    def dfs(x, y, d) :
        while True:
            visit[x][y][d] = 1
            if room[x][y] == 1 :
                if d % 2 :
                    d = (d + 2) % 4
            elif room[x][y] == 2 :
                if d % 2 == 0 :
                    d = (d + 2) % 4
            elif room[x][y] == 3 :
                if d % 2 :
                    d = (d - 1) % 4
                else :
                    d = (d + 1) % 4
            elif room[x][y] == 4 :
                if d % 2 :
                    d = (d + 1) % 4
                else :
                    d = (d - 1) % 4
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < M and not visit[nx][ny][d]:
                x = nx
                y = ny
            else :
                break
    for sx, sy in starts :
        for i in range(4) :
            visit[sx][sy][i] = 1
        for i in range(4) :
            nx = sx + dx[i]
            ny = sy + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visit[nx][ny][i]:
                dfs(nx, ny, i)
    
    answer = 0
    for i in range(N) :
        for j in range(M) :
            for k in range(4) :
                if visit[i][j][k] :
                    answer += 1
                    break
    return answer

if __name__ == "__main__" :
    print(solution())