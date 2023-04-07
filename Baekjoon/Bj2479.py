# 2479 경로찾기 G3

import sys
from heapq import heappop, heappush


def H_length(a, b, K):
    temp = 0
    for i in range(K):
        temp += 1 if a[i] != b[i] else 0
    return temp


def solution():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    graph = [[] for _ in range(N)]
    codes = [list(input()) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            Hl = H_length(codes[i], codes[j], K)
            if Hl == 1:
                graph[i].append((j, Hl))
                graph[j].append((i, Hl))
    s, e = map(int, input().split())
    inf = sys.maxsize
    D = [inf] * N
    heap = [(0, s - 1)]
    route = [0] * N
    D[s - 1] = 0
    while heap:
        d, n = heappop(heap)
        for nn, nd in graph[n]:
            if n == nn:
                continue
            ndd = d + nd
            if ndd < D[nn]:
                heappush(heap, (ndd, nn))
                D[nn] = nd
                route[nn] = n
    if D[e - 1] == inf:
        print(-1)
        return
    ans = [e]
    while ans[-1] != s:
        ans.append(route[ans[-1] - 1] + 1)
    print(*ans[::-1])


if __name__ == "__main__":
    solution()
