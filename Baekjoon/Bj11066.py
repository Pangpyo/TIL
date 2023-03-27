# 11066 파일 합치기 G3

import sys


input = sys.stdin.readline
inf = sys.maxsize
for t in range(int(input())):
    N = int(input())
    nums = list(map(int, input().split()))
    D = [[0] * (N + 1) for _ in range(N + 1)]
    sums = [0] * (N + 1)
    for i in range(1, N + 1):
        sums[i] = sums[i - 1] + nums[i - 1]
    for d in range(1, N):
        for dx in range(1, N - d + 1):
            dy = dx + d
            D[dx][dy] = inf
            for i in range(dx, dy):
                D[dx][dy] = min(
                    D[dx][dy], D[dx][i] + D[i + 1][dy] + sums[dy] - sums[dx - 1]
                )

    print(D[1][-1])
