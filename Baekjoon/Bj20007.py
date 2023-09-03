# 20007 떡 돌리기 G4

from heapq import heappop, heappush
import sys


def solution() :
    input = sys.stdin.readline
    N, M, X, Y = map(int, input().split())
    graph = [[] for _ in range(N)]
    for i in range(M) :
        u, v, d = map(int, input().split())
        graph[u].append((v, d))
        graph[v].append((u, d))
    heap = [(0, Y)]    
    inf = sys.maxsize
    D = [inf]*N
    D[Y] = 0
    while heap :
        d, n = heappop(heap)
        if D[n] < d :
            continue
        for nn, nd in graph[n] :
            ndd = nd + d
            if ndd < D[nn] :
                D[nn] = ndd
                heappush(heap, (ndd, nn))
    D.sort()
    day = 1
    dis = 0
    for d in D :
        d *= 2
        if d > X :
            return -1
        if dis + d > X :
            day += 1
            dis = 0
        dis += d
    return day

if __name__ == "__main__" :
    print(solution())