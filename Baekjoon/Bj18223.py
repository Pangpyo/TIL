# 18223 민준이와 마산 그리고 건우 G4

from heapq import heappop, heappush
import sys


def solution() :
    input = sys.stdin.readline
    V, E, P = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    for _ in range(E) :
        u, v, d = map(int, input().split())
        graph[u].append((v, d))
        graph[v].append((u, d))
    
    def dijkstra(s) :
        heap = [(0, s)]
        inf = sys.maxsize
        D = [inf]*(V+1)
        D[s] = 0
        while heap :
            d, n = heappop(heap)
            if D[n] < d :
                continue
            for nn, nd in graph[n] :
                ndd = d + nd
                if ndd < D[nn] :
                    heappush(heap, (ndd, nn))
                    D[nn] = ndd
        return D
    answer = "GOOD BYE"
    Ds = dijkstra(1)
    Dg = dijkstra(P)
    if Ds[-1] == Dg[1] + Dg[-1] :
        answer = "SAVE HIM"

    return answer

if __name__ == "__main__" :
    print(solution())