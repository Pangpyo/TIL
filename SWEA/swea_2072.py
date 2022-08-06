# 2072. 홀수만 더하기 D1

import sys


sys.stdin = open('input.txt')

T = int(input())

for i in range(1, T+1) :
    nums = list(map(int, input().split()))
    ans = 0
    for j in nums :
        if j%2 == 1 :
            ans += j
    print('#%d'%i, ans)