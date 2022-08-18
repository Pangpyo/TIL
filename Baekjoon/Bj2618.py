# 2618 종이자르기 S5

import sys


sys.stdin = open('input.txt')

N, M = map(int, input().split())
w = [0]
l = [0]
for _ in range(int(input())) :
    a, b = map(int, input().split())
    if a == 0 :
        l.append(b)
    else :
        w.append(b)
w.append(N)
w.sort()
l.append(M)
l.sort()
maxarea = 0
for i in range(1, len(w)) :
    n = w[i] - w[i-1]
    for j in range(1, len(l)) :
        m = l[j] - l[j-1]
        maxarea = n*m if n*m > maxarea else maxarea
print(maxarea)
