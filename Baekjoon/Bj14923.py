# 14923 미로 탈출 G4

from collections import deque
import sys


def solution() :
    input = sys.stdin.readline
    N, M = map(int, input().split())
    hx, hy = map(int, input().split())
    ex, ey = map(int, input().split())

    miro = [list(map(int, input().split())) for _ in range(N)]

    visit = [[[0, 0] for _ in range(M)] for _ in range(N)]

    que = deque()
    que.append((hx-1, hy-1, 0))
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    while que :
        x, y, flag = que.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= N or nx < 0 or ny >= M or ny < 0 :
                continue
            if visit[nx][ny][flag] :
                continue
            if miro[nx][ny] :
                if not flag :
                    que.append((nx, ny, 1))
                visit[nx][ny][1] = visit[x][y][flag] + 1
            else :
                que.append((nx, ny, flag))
                visit[nx][ny][flag] = visit[x][y][flag] + 1
    answer = min(visit[ex-1][ey-1])
    
    return answer if answer else -1

if __name__ == "__main__" :
    print(solution())