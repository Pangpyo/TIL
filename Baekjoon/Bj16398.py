# 16398 행성 연결 G4

import sys

def solution() :
    input = sys.stdin.readline
    N = int(input())
    ans = 0
    lines = []

    for u in range(N) :
        temp = list(map(int, input().split()))
        for v in range(u+1, N) :
            lines.append((u, v, temp[v]))
    lines.sort(key = lambda x : x[2])

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
        if union(u, v) :
            ans += d 
        if parent[0] == -N :
            break
    return ans

if __name__ == "__main__" :
    print(solution())