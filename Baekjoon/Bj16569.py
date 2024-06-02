# 16569 화산쇄설류 G4

from collections import deque
import sys


def solution():
    input = sys.stdin.readline
    N, M, V = map(int, input().split())
    X, Y = map(lambda x:int(x)-1, input().split())
    map_ = tuple(tuple(map(int, input().split())) for _ in range(N))
    volcano = [tuple(map(int, input().split())) for _ in range(V)]
    volcano.sort(key=lambda x: x[2])
    INF = sys.maxsize
    magma = [[INF]*M for _ in range(N)]
    dx = (-1, 0, 1, 0)
    dy = (0, 1, 0, -1)
    def eruption(x, y, t):
        que = deque()
        que.append((x, y, t))
        magma[x][y] = 0
        while que:
            x, y, t = que.popleft()
            nt = t + 1
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= N or ny < 0 or ny >= M:
                    continue
                if magma[nx][ny] <= nt:
                    continue
                magma[nx][ny] = nt
                que.append((nx, ny, nt))
    for x, y, t in volcano:
        eruption(x-1, y-1, t)
    visit = [[-1]*M for _ in range(N)]
    que = deque()
    que.append((X, Y))
    visit[X][Y] = 0
    while que:
        x, y = que.popleft()
        nt = visit[x][y] + 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if magma[nx][ny] <= nt:
                continue
            if visit[nx][ny] != -1:
                continue
            visit[nx][ny] = nt
            que.append((nx, ny))
    answer = (0, 0)
    for i in range(N):
        for j in range(M):
            if visit[i][j] == -1:
                continue
            if map_[i][j] > answer[0]:
                answer = (map_[i][j], visit[i][j])
    return answer

if __name__ == "__main__":
    print(*solution())