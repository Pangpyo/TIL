# 7511 소셜 네트워킹 어플리케이션 G5

import sys


def solution() :
    n = int(input())
    k = int(input())
    parent = list(range(n+1))
    def find(x) :
        if x == parent[x] :
            return x
        y = find(parent[x])
        parent[x] = y 
        return y 
    
    def union(x, y) :
        x = find(x)
        y = find(y)
        if x == y :
            return
        parent[max(x, y)] = parent[min(x, y)]
    
    for i in range(k) :
        union(*map(int, input().split()))
    m = int(input())
    ans = [0]*m
    for i in range(m) :
        u, v = map(int, input().split())
        ans[i] = (int(find(u)==find(v)))
    return ans

if __name__ == "__main__" :
    input = sys.stdin.readline
    for t in range(1, int(input())+1) :
        print(f"Scenario {t}:")
        print(*solution(), sep='\n')
        print()