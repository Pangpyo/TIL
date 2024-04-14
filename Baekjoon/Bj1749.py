# 1749 점수 따먹기 G4

import sys


def solution():
    input = sys.stdin.readline 
    N, M = map(int, input().split())
    matrix = tuple(tuple(map(int, input().split())) for _ in range(N))
    prefix_sum = [[0]*(M+1) for _ in range(N+1)]
    for i in range(N):
        for j in range(M):
            prefix_sum[i+1][j+1] = prefix_sum[i+1][j] + prefix_sum[i][j+1] - prefix_sum[i][j] + matrix[i][j]
    answer = -sys.maxsize
    for i in range(1, N+1):
        for j in range(1, M+1):
            ps = prefix_sum[i][j]
            for x in range(i):
                for y in range(j):
                    answer = max(answer, ps - prefix_sum[i][y] - prefix_sum[x][j] + prefix_sum[x][y])
    return answer

if __name__ == "__main__":
    print(solution())