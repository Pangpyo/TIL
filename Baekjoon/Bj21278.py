# 21278 호석이 두 마리 치킨 G5

import sys


def solution():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    INF = sys.maxsize
    D = [[INF if i!=j else 0 for j in range(N+1)] for i in range(N+1)]
    for _ in range(M):
        u, v = map(int, input().split())
        D[u][v] = 1
        D[v][u] = 1
    for k in range(1, N+1):
        for i in range(1, N+1):
            if i == k:
                continue
            for j in range(1, N+1):
                D[i][j] = min(D[i][j], D[i][k]+D[k][j])
    answer = [0, 0, INF]
    for i in range(1, N+1):
        for j in range(i+1, N+1):
            temp = [INF]*N
            for k in range(1, N+1):
                temp[k-1] = min(D[i][k], D[j][k])
            dist = sum(temp)*2
            if dist < answer[2]:
                answer[0] = i
                answer[1] = j
                answer[2] = dist
    return answer

if __name__ == "__main__":
    print(*solution())