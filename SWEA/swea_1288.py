# 1288. 새로운 불면증 치료법 D2

import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for i in range(1, T+1) :
    n = int(input())
    A = []
    a = 1
    while 1 :
        for j in str(n*a) :
            if int(j) not in A :
                A.append(int(j))
        if len(A) == 10 :
            break
        a +=1
    print('#%d'%i, str(n*a))
