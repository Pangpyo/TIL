# 15650 N과 M (2) S3

from itertools import combinations

N, M = map(int, input().split())

ans = combinations(list(range(1, N+1)), M)

for i in ans :
    print(*i)