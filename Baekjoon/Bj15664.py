# 15664 N과 M(10) S2

from itertools import combinations

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
ans = sorted(list(set(combinations(nums, M))))

for i in ans :
    print(*i)