# 2473 세 용액 G3


N = int(input())

nums = list(map(int, input().split()))

nums.sort()

ans = (1e10 * 3, ())
for i in range(N):
    a = i + 1
    b = N - 1
    while a < b:
        three = nums[i] + nums[a] + nums[b]
        if abs(three) < ans[0]:
            ans = (abs(three), (nums[i], nums[a], nums[b]))
        if three < 0:
            a += 1
        else:
            b -= 1
print(*ans[1])
