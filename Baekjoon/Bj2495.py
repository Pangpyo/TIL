# 2495 연속구간 B2

import sys

sys.stdin = open('input.txt')

for _ in range(3) :
    cnt = 1
    cntlist = []
    prenum = ''
    nums = input()
    for i in range(8) :
        if  prenum == nums[i] :
            cnt += 1
        if i == 7 or prenum != nums[i]:
            cntlist.append(cnt)
            cnt = 1
        prenum = nums[i]
    print(max(cntlist))
