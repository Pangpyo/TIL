# 24391 귀찮은 해강이 G5

import sys


def solution() :
    input = sys.stdin.readline
    N, M = map(int, input().split())
    parent = list(range(N+1))

    def find(x) :
        if parent[x] == x :
            return x
        y = find(parent[x])
        parent[x] = y
        return y

    def union(x, y) :
        x = find(x)
        y = find(y)
        if x != y :
            parent[max(x, y)] = min(x, y)

    for _ in range(M) :
        u, v = map(int, input().split())
        union(u, v)
    
    A = tuple(map(int, input().split()))
    answer = 0

    for i in range(1, N) :
        if find(A[i]) != find(A[i-1]) :
            answer += 1

    return answer

if __name__ == "__main__" :
    print(solution())