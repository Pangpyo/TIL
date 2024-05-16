# 15924 욱제는 사과팬이야!! G5

import sys


def solution():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    ways = tuple(input().rstrip() for _ in range(N))
    D = [[1]*M for _ in range(N)]
    MOD = 1_000_000_009
    for i in range(N):
        for j in range(M):
            if ways[i][j] == 'E' or ways[i][j] == 'B':
                D[i][j+1] = (D[i][j+1] + D[i][j]) % MOD
            if ways[i][j] == 'S' or ways[i][j] == 'B':
                D[i+1][j] = (D[i+1][j] + D[i][j]) % MOD
    return D[-1][-1]

if __name__ == "__main__":
    print(solution())