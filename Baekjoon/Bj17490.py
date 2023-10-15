# 17490 일감호에 다리 놓기 G3

import sys


def solution() :
    input = sys.stdin.readline
    N, M, K = map(int, input().split())

    stons = list(map(int, input().split()))
    parents = [-1]*(N+1)

    def find(x) :
        if parents[x] < 0 :
            return x
        y = find(parents[x])
        parents[x] = y
        return y
    
    def union(x, y) :
        x = find(x)
        y = find(y)
        if x == y :
            return False
        
        parents[min(x, y)] += parents[max(x, y)]
        parents[max(x, y)] = min(x, y)
        return True

    broken = set(tuple(map(int, input().split())) for _ in range(M))
    for i in range(1, N+1) :
        j = i%N + 1
        if (i, j) in broken or (j, i) in broken :
            continue
        union(i, j)
    if -parents[1] == N :
        return "YES"

    lines = sorted(enumerate(stons, 1), key=lambda x : x[1])
    ans = 0
    for i, x in lines :
        if union(0, i) :
            ans += x
        if ans > K :
            break
        if -parents[0] == N+1 :
            return "YES"
    return "NO"

if __name__ == "__main__" :
    print(solution())