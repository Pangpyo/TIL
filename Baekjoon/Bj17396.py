# 17396 백도어 G5

from heapq import heappop, heappush
import sys


def solution() :
    input = sys.stdin.readline
    N, M = map(int, input().split())
    inf = sys.maxsize
    D = [inf]*N
    see = list(map(int, input().split()))
    for i in range(N-1) :
        if see[i] :
            D[i] = 0
    D[0] = 0
    graph = [[] for _ in range(N)]
    for _ in range(M) :
        u, v, d = map(int, input().split())
        graph[u].append((v, d))
        graph[v].append((u, d))
    heap = [(0, 0)]
    
    while heap :
        d, n = heappop(heap)
        if D[n] < d :
            continue
        for nn, nd in graph[n] :
            ndd = nd + d
            if ndd < D[nn] :
                D[nn] = ndd
                heappush(heap, (ndd, nn))
    ans = D[-1]
    return ans if ans != inf else -1

if __name__ == "__main__" :
    print(solution())