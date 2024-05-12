# 10216 Count Circle Groups G4

import sys


def solution():
    input = sys.stdin.readline
    T = int(input())
    answer = [0]*T
    def find(x):
        if parents[x] == x:
            return x
        y = find(parents[x])
        parents[x] = y
        return y
    def union(x, y, t):
        x = find(x)
        y = find(y)
        if x == y:
            return
        parents[max(x, y)] = min(x, y)
        answer[t] -= 1
    
    for t in range(T):
        N = int(input())
        P = tuple(tuple(map(int, input().split())) for _ in range(N))
        parents = list(range(N))
        answer[t] = N
        for i in range(N):
            for j in range(i+1, N):
                if (P[i][0] - P[j][0])**2 + (P[i][1] - P[j][1])**2 <= (P[i][2]+P[j][2])**2:
                    union(i, j, t)
    return answer

if __name__ == "__main__":
    print(*solution(), sep='\n')