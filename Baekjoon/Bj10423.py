# 10423 전기가 부족해 G2

import sys


def solution() :
    input = sys.stdin.readline
    N, M, K = map(int, input().split())
    parent = [-1]*(N+1)
    power = list(map(int, input().split()))

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
    
    for i in range(1, K) :
        union(power[0], power[i])
    
    lines = [tuple(map(int, input().split())) for _ in range(M)]
    lines.sort(key = lambda x : (x[2]))
    answer = 0
    for u, v, w in lines :
        if union(u, v) :
            answer += w

    return answer

if __name__ == "__main__" :
    print(solution())