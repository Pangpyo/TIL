# 2206 벽 부수고 이동하기 G3

from collections import deque
import sys

sys.stdin = open('input.txt')

N, M = map(int, input().split())

graph = [list(map(int, input())) for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs() :
    visit = [[0]*M for _ in range(N)]
    visit[0][0] = 1
    que = deque([(0, 0, 0)]) # x좌표, y좌표, 거리, 벽을 부쉈는지 여부
    visitrecord = set()
    while que :
        x, y, crush = que.popleft()
        if x == N-1 and y == M-1 :
            return visit[-1][-1]
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= N or nx < 0 or ny >= M or ny < 0 :
                continue
            if (nx, ny, crush) in visitrecord:
                continue
            if graph[nx][ny] == 0 :
                visit[nx][ny] = visit[x][y] + 1
                que.append((nx, ny, crush))
                visitrecord.add((nx, ny, crush))
            else :
                if crush :
                    continue
                else :
                    visit[nx][ny] = visit[x][y] + 1
                    que.append((nx, ny, 1))
                    visitrecord.add((nx, ny, 1))
    return -1
print(bfs())
