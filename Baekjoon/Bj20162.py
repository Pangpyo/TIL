# 20162 간식 파티 S2

import sys


def solution():
    input = sys.stdin.readline
    N = int(input())
    nums = [0] + [int(input()) for _ in range(N)]
    D = [0]*(N+1)
    for i in range(1, N+1):
        for j in range(0, i):
            if nums[j] < nums[i]:
                D[i] = max(D[i], D[j] + nums[i])
    return max(D)

if __name__ == "__main__":
    print(solution())