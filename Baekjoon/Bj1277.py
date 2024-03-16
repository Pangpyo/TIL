# 1277 발전소 설치 G4

from heapq import heappop, heappush
import sys


def solution() :
    input = sys.stdin.readline
    N, M = map(int, input().split())
    L = float(input())
    powers = tuple(tuple(map(int, input().split())) for _ in range(N))
    inf = sys.maxsize
    D = [inf]*(N)
    D[0] = 0
    graph = [set() for _ in range(N)]
    for _ in range(M) :
        u, v = map(lambda x : int(x)-1, input().split())
        graph[u].add(v)
        graph[v].add(u)
    
    heap = [(0, 0)]
    
    def distance(n, nn) :
        x, y = powers[n]
        nx, ny = powers[nn]
        if nn in graph[n] :
            return 0
        return ((x-nx)**2+(y-ny)**2)**0.5

    while heap :
        d, n = heappop(heap)
        if d > D[n] :
            continue
        for nn in range(N) :
            nd = distance(n, nn)
            if nd >= L :
                continue
            ndd = nd + d
            if ndd < D[nn] :
                D[nn] = ndd
                heappush(heap, (ndd, nn))
    return int(D[-1]*1000)

if __name__ == "__main__" :
    print(solution())