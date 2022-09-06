# 1744 수 묶기 G4


import sys

sys.stdin = open('input.txt')
from collections import deque
K = int(input())
nums = []
for i in range(K) :
    nums.append(int(input()))
nums = deque(sorted(nums))

ans = []
check = 0
while len(nums) :
    if nums[-1] > 1 :
        a = nums.pop()
    else :
        a = nums.popleft()
    if check == 0 :
        ans.append(a)
        check = 1
    else : 
        if ans[-1]*a > (ans[-1]+a) :
            ans[-1] *= a
            check = 0
        else :
            ans.append(a)
            check = 1
print(sum(ans))