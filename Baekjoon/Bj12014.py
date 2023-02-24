# 12014 주식 G2

import sys
from bisect import bisect_left as bl
input = sys.stdin.readline

for t in range(1, int(input())+1) :
    N, K = map(int, input().split())
    nums = list(map(int, input().split()))
    D = [nums[0]]
    for i in range(1, N) :
        if nums[i] > D[-1] :
            D.append(nums[i])
        else :
            D[bl(D, nums[i])] = nums[i]
    
    ans = 1 if len(D) >= K else 0
    print(f'Case #{t}\n{ans}')