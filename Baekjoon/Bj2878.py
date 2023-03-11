# 2878 캔디캔디 G2
import sys


input = sys.stdin.readline

M, N = map(int, input().split())

nums = [int(input()) for _ in range(N)]

nums.sort(reverse=True)
nums.append(0)
ans = 0
t = 1 << 64
for i in range(N):
    temp = (nums[i] - nums[i + 1]) * (i + 1)
    now = nums[i]
    if temp <= M:
        M -= temp
    else:
        a = M % (i + 1)
        b = M // (i + 1)
        for j in range(N):
            nnow = 0
            if j < a:
                nnow = now - 1 - b
            elif j <= i:
                nnow = now - b
            else:
                nnow = nums[j]
            ans += nnow * nnow % t
        break

print(ans % t)
