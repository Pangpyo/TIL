# 17270 연예인은 힘들어 G3

import sys
from heapq import heappop, heappush

def solution() :
    input = sys.stdin.readline
    V, M = map(int, input().split())
    inf = sys.maxsize
    graph = [[inf for _ in range(V+1)] for _ in range(V+1)]
    for _ in range(M) :
        a, b, c = map(int, input().split())
        graph[a][b] = min(graph[a][b], c)
        graph[b][a] = min(graph[b][a], c)
    
    locs = tuple(map(int, input().split()))
    
    D = [[inf, inf] for _ in range(V+1)]
    for i in range(2) :
        heap = []
        heappush(heap, (0, locs[i]))
        D[locs[i]][i] = 0
        while heap :
            d, n = heappop(heap)
            if d > D[n][i] :
                continue
            for nn in range(1, V+1) :
                if graph[nn] == inf :
                    continue
                ndd = graph[n][nn] + d
                if ndd < D[nn][i] :
                    D[nn][i] = ndd
                    heappush(heap, (ndd, nn))
    dist = inf
    dist_to = inf
    ans = -1
    ans_list = []
    for i in range(1, V+1) :
        if i in locs or D[i][0] == inf or D[i][1] == inf:
            continue
        dist = min(sum(D[i]), dist)
        ans_list.append(i)
    for i in ans_list :
        if sum(D[i]) == dist and D[i][1] >= D[i][0] and dist_to > D[i][0]:
            dist_to = D[i][0]
            ans = i
    return ans

if __name__ == "__main__" :
    print(solution())