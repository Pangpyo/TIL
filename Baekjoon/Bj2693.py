# 2693 N번째 큰 수 B1

import sys


sys.stdin = open('input.txt')

T = int(input())

for i in range(T) :
    A = list(map(int, input().split()))
    print(sorted(A)[-3])