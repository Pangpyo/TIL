# 9694 무엇을 아느냐가 아니라 누구를 아느냐가 문제다 G3
import sys
from heapq import heappop, heappush

input = sys.stdin.readline


def dijkstra():
    inf = sys.maxsize
    D = [inf] * M
    D[0] = 0
    heap = [(0, 0)]
    route = [-1] * M
    while heap:
        d, n = heappop(heap)
        for nn, nd in graph[n]:
            ndd = nd + d
            if ndd < D[nn]:
                D[nn] = ndd
                route[nn] = n
                heappush(heap, (ndd, nn))
    ans = []
    idx = M - 1
    while 1:
        if route[idx] != -1:
            ans.append(idx)
            idx = route[idx]
        else:
            break
    if ans:
        return [0] + ans[::-1]
    else:
        return [-1]


for t in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    graph = [[] for _ in range(M)]
    for i in range(N):
        u, v, d = map(int, input().split())
        graph[u].append((v, d))
        graph[v].append((u, d))
    ans = dijkstra()
    print(f"Case #{t}:", end=" ")
    print(*ans)
