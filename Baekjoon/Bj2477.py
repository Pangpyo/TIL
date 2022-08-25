# 2477 참외밭 S3

import sys

sys.stdin = open('input.txt')

K = int(input())

side = []

x = []
y = []
for i in range(6) :
    d, l = map(int, input().split())
    side.append(l)
    if d == 1 or d == 2 :
        x.append(l)
    else :
        y.append(l)

bigsq = max(x)*max(y)
maxidx = side.index(max(x))
mayidx = side.index(max(y))
minx = abs(side[(maxidx-1)%6]-side[(maxidx+1)%6])
miny = abs(side[(mayidx-1)%6]-side[(mayidx+1)%6])
smallsq = minx*miny

print((bigsq-smallsq)*K)