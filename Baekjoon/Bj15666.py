# 15666 N과 M(12) S2

from itertools import combinations_with_replacement

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
ans = sorted(list(set(combinations_with_replacement(nums, M))))

for i in ans :
    print(*i)