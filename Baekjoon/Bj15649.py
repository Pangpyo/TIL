# 15649 N과 M(1) S3

from itertools import permutations

N, M = map(int, input().split())

ans = permutations(list(range(1, N+1)), M)

for i in ans :
    print(*i)