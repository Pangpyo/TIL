# 5557 1학년 G5

from collections import defaultdict


N = int(input())

nums = list(map(int, input().split()))

result = nums.pop()

cnt = 0


D = [defaultdict(int) for _ in range(N - 1)]


D[0][nums[0]] = 1

for i in range(1, N - 1):
    for n, cnt in D[i - 1].items():
        if n + nums[i] <= 20:
            D[i][n + nums[i]] += cnt
        if n - nums[i] >= 0:
            D[i][n - nums[i]] += cnt

print(D[-1][result])
