# 17940 지하철 G4

from heapq import heappop, heappush
import sys

def solution() : 
    input = sys.stdin.readline
    N, M = map(int, input().split())
    C = [int(input()) for _ in range(N)]
    E = [list(map(int, input().split())) for _ in range(N)]
    inf = sys.maxsize
    D = [[inf, inf] for _ in range(N)]
    D[0] = [0, 0]
    heap = [(0, 0, 0)]
    while heap :
        trs, tm, n = heappop(heap)
        c = C[n]
        if trs > D[n][0] :
            continue
        if tm > D[n][1] :
            continue
        for nn in range(N) :
            if not E[n][nn] :
                continue
            nc = C[nn]
            ntrs = trs + int(c != nc)
            ntm = tm + E[n][nn]
            if D[nn][0] >= ntrs and D[nn][1] > ntm :
                heappush(heap, (ntrs, ntm, nn))
                D[nn][0] = ntrs
                D[nn][1] = ntm


    return D[M]

if __name__ == "__main__" :
    print(*solution())