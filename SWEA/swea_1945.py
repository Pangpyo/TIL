# 1945 간단한 소인수분해 D2

import sys

sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1) :
    factors = [0]*5 # 각 인덱스의 a, b, c, d, e가 들어간다.
    N = int(input())
    while 1 : 
        if N%2 == 0 : # 2 3 5 7 11이 약수로 존재할 경우 나눠준 후 각 값을 factors에 반환한다.
            N = N/2
            factors[0] += 1
        if N%3 == 0 :
            N = N/3
            factors[1] += 1
        if N%5 == 0 :
            N = N/5
            factors[2] += 1
        if N%7 == 0 :
            N = N/7
            factors[3] += 1
        if N%11 == 0 :
            N = N/11
            factors[4] += 1
        if N == 1 : # 더 이상 약수가 없을 경우 break한다.
            break
    print('#%d'%t, *factors)