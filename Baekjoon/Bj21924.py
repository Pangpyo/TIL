# 21924 도시 건설 G4 

import sys


def solution() :
    input = sys.stdin.readline
    N, M = map(int, input().split())
    ans = 0
    lines = []
    for i in range(M) :
        u, v, d = map(int, input().split())
        ans += d
        lines.append((u, v, d))
    lines.sort(key=lambda x : x[2])
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
        if x == y :
            return False
        parent[min(x, y)] += parent[max(x, y)]
        parent[max(x, y)] = min(x, y)
        return True
    
    for u, v, d in lines :
        if union(u-1, v-1) :
            ans -= d
        if parent[0] == -N :
            return ans
    return -1
    
if __name__ == "__main__" :
    print(solution())