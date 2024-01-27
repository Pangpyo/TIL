# 20046 Road Reconstruction G4

from heapq import heappop, heappush
import sys


def solution() :
    input = sys.stdin.readline
    N, M = map(int, input().split())
    road = tuple(tuple(map(int, input().split())) for _ in range(N))
    if road[0][0] == -1 :
        return -1
    heap = [(road[0][0], 0, 0)]
    INF = sys.maxsize
    D = [[INF]*M for _ in range(N)]
    D[0][0] = road[0][0]
    dx = (0, 1, 0, -1)
    dy = (1, 0, -1, 0)
    while heap :
        d, x, y = heappop(heap)
        if d > D[x][y] :
            continue
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= N or nx < 0 or ny >= M or ny < 0 :
                continue
            if road[nx][ny] == -1 :
                continue
            nd = road[nx][ny] + d
            if nd < D[nx][ny] :
                D[nx][ny] = nd
                heappush(heap, (nd, nx, ny))

    return D[-1][-1] if D[-1][-1] != INF else -1

if __name__ == "__main__" :
    print(solution())