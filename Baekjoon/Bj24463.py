# 24463 미로 G4

from collections import deque
import sys


def solution() :
    input = sys.stdin.readline
    sys.setrecursionlimit(10**8)
    N, M = map(int, input().split())
    miro = [list(input().rstrip()) for _ in range(N)]

    
    dx = (-1, 0, 1, 0)
    dy = (0, 1, 0, -1)
    def getStart():
        sx, sy = 0, 0
        for i in range(N) :
            for j in range(M) :
                if miro[i][j] == '.' :
                    que = deque()
                    que.append((i, j))
                    visit = [[0]*M for _ in range(N)]
                    visit[i][j] = 1
                    while que :
                        x, y = que.popleft()
                        for i in range(4) :
                            nx = x + dx[i]
                            ny = y + dy[i]
                            if nx >= N or nx < 0 or ny >= M or ny < 0 :
                                return x, y
                            if visit[nx][ny] or miro[nx][ny] == '+':
                                continue
                            visit[nx][ny] = 1
                            que.append((nx, ny))
                    break
        return sx, sy
    
    sx, sy = getStart()
    ex, ey = 0, 0
    def bfs(sx, sy) :
        nonlocal ex, ey
        que = deque()
        que.append((sx, sy))
        visit = [[-1]*M for _ in range(N)]
        visit[sx][sy] = -2
        while que :
            x, y = que.popleft()
            for i in range(4) :
                nx = x + dx[i]
                ny = y + dy[i]
                if nx >= N or nx < 0 or ny >= M or ny < 0 :
                    if (x, y) != (sx, sy) :
                        ex, ey = x, y
                        return visit
                    continue
                if visit[nx][ny] != -1 or miro[nx][ny] == '+':
                    continue
                visit[nx][ny] = (i+2)%4
                que.append((nx, ny))
        return visit
    visit = bfs(sx, sy)
    x, y = ex, ey
    for i in range(N):
        for j in range(M):
            if miro[i][j] == '.':
                miro[i][j] = '@' 
    while True :
        miro[x][y] = '.'
        if visit[x][y] == -2:
            break
        d = visit[x][y]
        x = x + dx[d]
        y = y + dy[d]
    answer = '\n'.join(map(''.join, miro))
    return answer

if __name__ == "__main__" :
    print(solution(), sep='\n')