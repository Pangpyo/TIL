# 2194 유닛 이동시키기 G4

from collections import deque
import sys


def solution():
    input = sys.stdin.readline
    N, M, A, B, K = map(int, input().split())
    map_ = [[0]*M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        map_[x-1][y-1] = 1
    INF = sys.maxsize
    visit = [[INF]*M for _ in range(N)]
    sx, sy = map(lambda x: int(x)-1, input().split())
    ex, ey = map(lambda x: int(x)-1, input().split())
    def can_move(x, y):
        for i in range(A):
            for j in range(B):
                if x+i >= N or x < 0 or y + j >= M or y < 0:
                    return False
                if map_[x+i][y+j]:
                    return False
        return True
    visit[sx][sy] = 0
    que = deque()
    que.append((sx, sy))
    dx = (-1, 0, 1, 0)
    dy = (0, 1, 0, -1)
    while que:
        x, y = que.popleft()
        d = visit[x] [y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not can_move(nx, ny):
                continue
            if visit[nx][ny] <= d+1:
                continue
            visit[nx][ny] = d+1
            if (nx, ny) == (ex, ey):
                return visit[nx][ny]
            que.append((nx, ny))
    return -1

if __name__ == "__main__":
    print(solution())