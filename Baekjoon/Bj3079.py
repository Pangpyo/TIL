# 3079 입국심사 G5

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

P = [int(input()) for _ in range(n)]
s = 0
e = max(P) * m
ans = 0
while s <= e:
    mid = (s + e) // 2
    cnt = 0
    for p in P:
        cnt += mid // p
    if cnt >= m:
        e = mid - 1
        ans = mid
    else:
        s = mid + 1
print(ans)
