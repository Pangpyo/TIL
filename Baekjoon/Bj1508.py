# 1508 레이스 G2

N, M, K = map(int, input().split())

D = list(map(int, input().split()))

s = 1
e = N
ans = 0
while s <= e:
    mid = (s + e) // 2
    pre = D[0]
    cnt = 1
    visit = 1 << (K - 1)
    for i in range(1, K):
        if D[i] - pre >= mid:
            pre = D[i]
            cnt += 1
            visit = visit | 1 << (K - 1 - i)
        if cnt == M:
            break
    if cnt >= M:
        s = mid + 1
        ans = visit
    else:
        e = mid - 1

print(format(ans, "b"))
