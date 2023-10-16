# 17250 은하철도 G4

import sys


def solution() :
    input = sys.stdin.readline
    N, M = map(int, input().split())
    parents = [-int(input()) for _ in range(N)]

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
            return parents[x]
        x, y = min(x, y), max(x, y)
        parents[x] += parents[y]
        parents[y] = x
        return parents[x]
    ans = [0]*M
    for i in range(M) :
        u, v = map(lambda x : int(x)-1, input().split())
        ans[i] = -union(u, v)
    return ans

if __name__ == "__main__" :
    print(*solution(), sep='\n')