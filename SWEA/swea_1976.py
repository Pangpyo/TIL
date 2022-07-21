# 1976. 시각 덧셈 D2

import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for i in range(1, T+1) :
    t1, m1, t2, m2 = map(int, input().split())
    t = t1 + t2 
    m = m1 + m2
    if m > 60 :
        t +=1
        m -= 60
    if t > 12 :
        t -= 12
    print('#%d'%i, t, m)
