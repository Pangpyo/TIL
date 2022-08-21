# 15655 N과 M(6) S3

from itertools import combinations

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
ans = combinations(nums, M)

for i in ans :
    print(*i)