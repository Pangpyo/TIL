# 2068. 최대수 구하기 D1

import sys

sys.stdin = open('input.txt')

T = int(input())

for i in range(1, T+1) :
    nums = list(map(int, input().split()))
    print('#%d'%i, max(nums))