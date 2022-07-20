# 1284. 수도 요금 경쟁 D2 

import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for i in range(1, T+1) :
    P, Q, R, S, W = map(int, input().split())
    A = W*P
    B = Q if W<=R else Q+(W-R)*S
    print('#%d'%i, min([A, B]))