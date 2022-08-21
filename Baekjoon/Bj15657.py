# 15657 N과 M(8) S3

from itertools import combinations_with_replacement

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
ans = combinations_with_replacement(nums, M)

for i in ans :
    print(*i)