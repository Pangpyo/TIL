# 2830 행성X3 G3

import sys

input = sys.stdin.readline

N = int(input())
bits = [0] * 20
ans = 0
for i in range(N):
    temp = int(input())
    for j in range(20):
        n = 1 << j
        if n & temp:
            bits[j] += 1

for i in range(20):
    ans += (N - bits[i]) * bits[i] * (1 << i)

print(ans)
