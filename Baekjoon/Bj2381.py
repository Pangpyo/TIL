# 2381 최대거리 G3

import sys


input = sys.stdin.readline

N = int(input())

p = []
m = []


for i in range(N):
    x, y = map(int, input().split())
    p.append(x + y)
    m.append(x - y)
p.sort()
m.sort()
print(max(p[-1] - p[0], m[-1], m[0]))
