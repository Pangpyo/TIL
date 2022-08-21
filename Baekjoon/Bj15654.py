# 15654 N과 M(5) S3

from itertools import permutations


N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
ans = permutations(nums, M)

for i in ans :
    print(*i)