# 20303 할로윈의 양아치 G3

import sys


def solution() :
    input = sys.stdin.readline
    N, M, K = map(int, input().split())
    candy = list(map(int, input().split()))

    parent = [-1]*N
    def find(x) :
        if parent[x] < 0 :
            return x
        y = find(parent[x])
        parent[x] = y
        return y

    def union(x, y) :
        x = find(x)
        y = find(y)
        if x != y :
            parent[min(x, y)] += parent[max(x, y)]
            parent[max(x, y)] = min(x, y)
            candy[min(x, y)] += candy[max(x, y)]
            candy[max(x, y)] = 0
    for i in range(M) :
        a, b = map(int, input().split())
        union(a-1, b-1)
    D = [-1]*K
    D[0] = 0
    for i in range(N) :
        cnt, cost = parent[i], candy[i]
        if cnt >= 0 :
            continue
        cnt *= -1
        for j in reversed(range(K)) :
            if D[j] >= 0 and j+cnt < K:
                D[j+cnt] = max(D[j+cnt], D[j]+cost)
    return max(D)

if __name__ == "__main__" :
    print(solution())