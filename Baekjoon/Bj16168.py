# 16168 퍼레이드 G4

import sys


def solution() :
    input = sys.stdin.readline
    V, E = map(int, input().split())
    parents = [-1]*(V+1)
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
            return 
        parents[min(x, y)] += parents[max(x, y)]
        parents[max(x, y)] = min(x, y)
    
    degree = [0]*(V+1)

    for _ in range(E) :
        u, v = map(int, input().split())
        union(u, v)
        degree[u] += 1
        degree[v] += 1

    if parents[1] != -V :
        return "NO"
    
    count_odd = 0

    for d in degree :
        if d % 2 :
            count_odd += 1
    if count_odd == 0 or count_odd == 2 :
        return "YES"

    return "NO"

if __name__ == "__main__" :
    print(solution())