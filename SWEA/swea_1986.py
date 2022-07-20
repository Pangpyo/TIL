# 1986. 지그재그 숫자 D2

import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for i in range(1,T+1) :
    n = int(input())
    s = 0
    for j in range(1,n+1) :
        if j%2 == 1 :
            s += j
        else :
            s -= j
    print('#%d'%i, s)