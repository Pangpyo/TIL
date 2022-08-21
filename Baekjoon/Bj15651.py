# 15651 N과 M(3) S3

from itertools import product

N, M = map(int, input().split())

ans = product(list(range(1, N+1)), repeat=M) # 중복순열

for i in ans :
    print(*i)