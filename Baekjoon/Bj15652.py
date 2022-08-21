# 15652 N과 M(4) S3

from itertools import combinations_with_replacement

N, M = map(int, input().split())

ans = combinations_with_replacement(list(range(1, N+1)), M)

for i in ans :
    print(*i)