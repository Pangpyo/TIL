# 9325 얼마? B3

import sys


sys.stdin = open('input.txt')

T = int(input())

for i in range(T) :
    s = int(input())
    n = int(input())
    for j in range(n) :
        q, p = map(int, input().split())
        s += q*p
    print(s)