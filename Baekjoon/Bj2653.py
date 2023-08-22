# 2653 안정된 집단 G4

import sys


def solution() :
    input = sys.stdin.readline
    N = int(input())
    D = [list(map(int, input().split())) for _ in range(N)]
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
    
    for i in range(N) :
        for j in range(i+1, N) :
            if not D[i][j] :
                union(i, j)
    cnt = 0
    ans = []
    for i in range(N) :
        if parent[i] < 0 :
            if parent[i] == -1 :
                print(0)
                return 
            cnt += 1
            temp = [i+1]
            for j in range(i, N) :
                if parent[j] == i :
                    temp.append(j+1)
            ans.append(sorted(temp))
    ans.sort()
    print(cnt)
    for a in ans :
        print(*a)
    

if __name__ == "__main__" :
    solution()

