# 10986 나머지 합 G3

N, M = map(int, input().split())

A = list(map(int, input().split()))

D = [0] * N
nums = [0] * (M)
ans = 0
for i in range(N):
    D[i] = (D[i - 1] + A[i]) % M
    nums[D[i]] += 1
    if not D[i]:
        ans += 1
    if nums[D[i]]:
        ans += nums[D[i]] - 1


print(ans)
