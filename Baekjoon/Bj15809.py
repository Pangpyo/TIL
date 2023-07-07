# 15809 전국시대 G4

import sys


def solution() :
    input = sys.stdin.readline
    
    N, M = map(int, input().split())
    A = [0]*(N+1)
    for i in range(1, N+1) :
        A[i] = int(input())

    parent = [-1]*(N+1)

    def find(x) :
        if parent[x] <= 0 :
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
        A[min(x, y)] += A[max(x, y)]
        A[max(x, y)] = 0

    def war(x, y) :
        x = find(x)
        y = find(y)
        if A[x] > A[y] :
            A[x] -= A[y]
            A[y] = 0
            parent[x] += parent[y]
            parent[y] = x
        elif A[y] > A[x] :
            A[y] -= A[x]
            A[x] = 0
            parent[y] += parent[x]
            parent[x] = y
        else :
            A[y] = 0
            A[x] = 0
            parent[x] = 0
            parent[y] = 0
    
    for i in range(M) :
        O, P, Q = map(int, input().split())
        if O == 1 :
            union(P, Q)
        else :
            war(P, Q)

    A.sort()
    ans = []

    for a in A :
        if a :
            ans.append(a)
    return ans

if __name__ == "__main__" :
    ans = solution()
    print(len(ans))
    print(*ans)