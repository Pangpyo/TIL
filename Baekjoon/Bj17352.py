# 17353 여러분의 다리가 되어 드리겠습니다! G5

import sys


def solution() :
    input = sys.stdin.readline
    N = int(input())
    parent = [-1]*(N+1)
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
            return
        parent[min(x, y)] += parent[max(x, y)]
        parent[max(x, y)] = min(x, y)
    
    for i in range(N-2) :
        u, v = map(int, input().split())
        union(u, v)
    answer = []
    for i in range(1, N+1) :
        if parent[i] < 0 :
            answer.append(i)
    return answer

if __name__ == "__main__" :
    print(*solution())