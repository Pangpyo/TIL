# 14658 하늘에서 별똥별이 빗발친다 G3

import sys

input = sys.stdin.readline

N, M, L, K = map(int, input().split())

stars = [tuple(map(int, input().split())) for _ in range(K)]

ans = 0

xlist = []
ylist = []
for x, y in stars:
    xlist.append(x)
    ylist.append(y)

for sx in xlist:
    ex = sx + L
    for sy in ylist:
        ey = sy + L
        temp = 0
        for x, y in stars:
            if sx <= x <= ex and sy <= y <= ey:
                temp += 1
        ans = max(ans, temp)

print(K - ans)
