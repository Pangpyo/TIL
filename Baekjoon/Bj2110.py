import sys

# 2110 공유기 설치 G4

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
    for i in range(1, n):
        if P[i] - P[pre] >= mid:
            cnt += 1
            pre = i
    if cnt >= m:
        s = mid + 1

        ans = mid
    else:
        e = mid - 1

print(ans)
