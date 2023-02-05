# 2110 공유기 설치 G4
from bisect import bisect_left as bl
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

P = sorted([int(input()) for _ in range(n)])

s = 1
e = max(P) - min(P)
ans = 0
while s <= e:
    mid = (s + e) // 2
    cnt = 1
    pre = 0
    while 1:
        pre = bl(P, mid + P[pre])
        if pre >= n:
            break
        else:
            cnt += 1
    if cnt >= m:
        s = mid + 1
        ans = mid
    else:
        e = mid - 1

print(ans)
