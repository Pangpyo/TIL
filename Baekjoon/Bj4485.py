# 4485 녹색 옷 입은 애가 젤다지? G4

import sys
from heapq import heappop, heappush

input = sys.stdin.readline
t = 0
while 1:
    t += 1
    N = int(input())
    if not N:
        break
    cave = [list(map(int, input().split())) for _ in range(N)]

    heap = []

    heappush(heap, (cave[0][0], 0, 0))

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    D = [[10**5] * N for _ in range(N)]
    D[0][0] = cave[0][0]
    ans = 0
    while heap:
        cost, x, y = heappop(heap)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= N or nx < 0 or ny >= N or ny < 0:
                continue
            ncost = cost + cave[nx][ny]
            if ncost < D[nx][ny]:
                D[nx][ny] = ncost
                heappush(heap, (ncost, nx, ny))
    print(f"Problem {t}: {D[-1][-1]}")
