# 22116 창영이와 퇴근 G4

import sys
from heapq import heappop, heappush

def solution() :
    input = sys.stdin.readline
    N = int(input())
    A = [tuple(map(int, input().split())) for _ in range(N)]
    inf = sys.maxsize
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    heap = []
    heappush(heap, (0, 0, 0))
    D = [[inf]*N for _ in range(N)]
    D[0][0] = 0
    while heap :
        d, x, y = heappop(heap)
        if d > D[x][y] :
            continue
        h = A[x][y]
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= N or nx < 0 or ny >= N or ny < 0 :
                continue
            nd = max(d, abs(A[nx][ny] - h))
            if nd < D[nx][ny] :
                D[nx][ny] = nd
                heappush(heap, (nd, nx, ny))
    return D[-1][-1]

if __name__ == "__main__" :
    print(solution())