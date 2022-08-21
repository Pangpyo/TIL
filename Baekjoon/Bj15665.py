# 15665 N과 M(11) S2

from itertools import product

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
ans = sorted(list(set(product(nums, repeat=M))))

for i in ans :
    print(*i)