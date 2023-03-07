# 2342 Dance Dance Revolution G3

import sys

input = sys.stdin.readline
sl = 25

nums = list(map(int, input().split()))
N = len(nums) - 1

inf = sys.maxsize

D = [[inf] * (sl) for _ in range(N)]

D[0][1 | 1 << nums[0]] = 2


def score(a, b):
    if a == 0:
        return 2
    if abs(a - b) == 2:
        return 4
    if a == b:
        return 1
    return 3


for i in range(N - 1):
    b = nums[i + 1]
    for j in range(sl):
        if D[i][j] < inf:
            for a in range(5):
                if j & 1 << a:
                    temp = (j & ~(1 << a)) | 1 << b
                    D[i + 1][temp] = min(D[i + 1][temp], D[i][j] + score(a, b))

ans = inf
for i in range(25):
    ans = min(ans, D[-1][i])

print(ans)
