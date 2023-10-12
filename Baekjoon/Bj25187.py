# 25187 고인물이 싫어요 G4

import sys


def solution() :
    input = sys.stdin.readline
    N, M, Q = map(int, input().split())
    water = list(map(int, input().split()))
    parent = [i for i in range(N+1)]
    total_water = [0]*(N+1)
    for i in range(1, N+1) :
        total_water[i] = 1 if water[i-1] else -1
    def find(x) :
        if parent[x] == x :
            return x
        y = find(parent[x])
        parent[x] = y
        return y
    
    def union(x, y) :
        x = find(x)
        y = find(y)
        if x == y :
            return
        total_water[min(x, y)] += total_water[max(x, y)]
        parent[max(x, y)] = min(x, y)

    for _ in range(M) :
        u, v = map(int, input().split())
        union(u, v)
    answer = [0]*Q
    for q in range(Q) :
        x = find(int(input()))
        answer[q] = int(total_water[x] > 0)
    return answer

if __name__ == "__main__" :
    print(*solution(), sep='\n')
