# 14630 변신로봇 G3

from heapq import heappop, heappush
import sys


def solution() :
    input = sys.stdin.readline
    N = int(input())
    robots = tuple(input().rstrip() for _ in range(N))
    s, e = map(lambda x : int(x)-1, input().split())
    heap = [(0, s)]
    INF = sys.maxsize
    D = [INF]*N
    D[s] = 0
    def get_distance(n, nn) :
        d = 0
        for a, b in zip(robots[n], robots[nn]) :
            d += (int(a)-int(b))**2
        return d
    while heap :
        d, n = heappop(heap)
        if d > D[n] :
            continue
        for nn in range(N) :
            if n == nn :
                continue
            nd = get_distance(n, nn) + d
            if nd < D[nn] :
                D[nn] = nd
                heappush(heap, (nd, nn))
    
    return D[e]

if __name__ == "__main__" :
    print(solution())