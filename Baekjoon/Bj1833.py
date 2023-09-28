# 1833 고속철도 설계하기 G3

import sys


def solution() :
    input = sys.stdin.readline
    N = int(input())
    M = [list(map(int, input().split())) for _ in range(N)]
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
    ans = [[0, 0]]
    lines = []
    for i in range(N) :
        for j in range(i+1, N) :
            if M[i][j] < 0 :
                ans[0][0] -= M[i][j]
                union(i, j)
            elif M[i][j] > 0 :
                lines.append((M[i][j], i, j))
    lines.sort(key=lambda x : x[0])

    for d, u, v in lines :
        if union(u, v) :
            ans[0][0] += d
            ans[0][1] += 1
            ans.append((u+1, v+1))
        if parent[0] == N :
            break

    return ans

if __name__ == "__main__" :
    for sol in solution() :
        print(*sol)