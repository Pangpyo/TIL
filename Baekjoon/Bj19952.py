# 19953 인성 문제있어?? G4

from collections import deque
import sys


def solution() :
    N, M, O, F, sx, sy, ex, ey  = map(int, input().split())
    sx -= 1
    sy -= 1
    ex -= 1
    ey -= 1
    miro = [[0]*M for _ in range(N)]
    for _ in range(O) :
        x, y, h = map(int, input().split())
        miro[x-1][y-1] = h
    que = deque([(sx, sy, F)])
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0 ,-1]
    visit = [[0]*M for _ in range(N)]
    while que :
        x, y, f = que.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= N or nx < 0 or ny >= M or ny < 0 :
                continue
            if visit[nx][ny] or miro[nx][ny] - miro[x][y] > f :
                continue
            if (nx, ny) == (ex, ey) :
                return '잘했어!!'
            if f > 1 :
                visit[nx][ny] = 1
                que.append((nx, ny, f-1))
    return '인성 문제있어??'

if __name__ == "__main__" :
    input = sys.stdin.readline
    T = int(input())
    for i in range(T) :
        print(solution())