# 3020 개똥벌레 G5

import sys


input = sys.stdin.readline


N, H = map(int, input().split())


bottom = [0] * (H + 1)
top = [0] * (H + 1)

for i in range(N):
    if i % 2:
        bottom[int(input())] += 1
    else:
        top[int(input())] += 1

for i in range(H + 1):
    bottom[i] += bottom[i - 1]
    top[i] += top[i - 1]

temp = []
for h in range(H):
    b = bottom[h]

    t = top[H - 1 - h]

    temp.append(N - (b + t))


answer = [0, 0]
answer[0] = min(temp)
answer[1] = temp.count(answer[0])

print(*answer)
