# 15656 N과 M(7) S3

from itertools import product

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
ans = product(nums, repeat=M) # 중복순열

for i in ans :
    print(*i)