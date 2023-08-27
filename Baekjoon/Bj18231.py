# 18231 파괴된 도시 G5

import sys


def solution() :
    input = sys.stdin.readline
    N, M = map(int, input().split())
    graph = [set([i]) for i in range(N+1)]
    for _ in range(M) :
        u, v = map(int, input().split())
        graph[u].add(v)
        graph[v].add(u)
    K = int(input())
    P = set(map(int, input().split()))
    D = set()
    ans = []
    for n in P :
        if not graph[n] - P :
            D |= graph[n]
            ans.append(n)
    if D != P :
        print(-1)
    else :
        print(len(ans))
        print(*ans)

if __name__ == "__main__" :
    solution()