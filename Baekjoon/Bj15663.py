# 15663 N과 M(9) S2

from itertools import permutations

N, M = map(int, input().split())
nums = list(map(int, input().split()))
ans = sorted(list(set(permutations(nums, M))))

for i in ans :
    print(*i)