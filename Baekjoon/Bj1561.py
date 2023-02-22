# 1561 놀이 공원 G2

N, M = map(int, input().split())

atrs = list(map(int, input().split()))


s = 0
e = max(atrs) * N

while s <= e:
    mid = (s + e) // 2
    cnt = 0
    for i, atr in enumerate(atrs):
        cnt += mid // atr + 1
    if cnt >= N:
        e = mid - 1
        time = mid
    else:
        s = mid + 1

cnt = 0
for i, atr in enumerate(atrs):
    cnt += (time - 1) // atr + 1
ans = 0

for i, atr in enumerate(atrs):
    if time % atr == 0:
        ans = i + 1
        cnt += 1
        if cnt == N:
            break

print(ans)
