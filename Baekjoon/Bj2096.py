# 2096 내려가기 G5

import sys


def solution():
    input = sys.stdin.readline
    N = int(input())
    nums = tuple(tuple(map(int, input().split())) for _ in range(N))
    INF = sys.maxsize
    minD = nums[0]
    maxD = nums[0]
    for i in range(1, N):
        min_temp = [INF]*3
        max_temp = [0]*3
        for j in range(3):
            for k in (-1, 0, 1):
                jk = j + k
                if jk < 0 or jk >= 3:
                    continue
                max_temp[j] = max(max_temp[j], maxD[jk] + nums[i][j])
                min_temp[j] = min(min_temp[j], minD[jk] + nums[i][j])
        minD = min_temp
        maxD = max_temp
    return (max(maxD), min(minD))

if __name__ == "__main__":
    print(*solution())