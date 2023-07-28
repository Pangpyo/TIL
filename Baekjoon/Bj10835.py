# 10835 카드게임 G5

import sys


def solution() :
    sys.setrecursionlimit(10**6)
    input = sys.stdin.readline
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    D = [[-1]*(N+1) for _ in range(N+1)]
    def dfs(x, y):
        if x >= N or y >= N:
            return 0
        if D[x][y] != -1:
            return D[x][y]
        
        if A[x] > B[y]:
            D[x][y] = dfs(x, y+1) + B[y]
        else:
            D[x][y] = max(dfs(x+1, y) , dfs(x+1, y+1) )
        return D[x][y]
    
    return dfs(0, 0)

if __name__ == "__main__" :
    print(solution())