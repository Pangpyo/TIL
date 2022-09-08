# 5430 AC G5

from collections import deque
import sys

sys.stdin = open('input.txt')

for _ in range(int(input())) :
    p = list(input())
    n = int(input())
    s = input()
    a = ''
    nums = deque()
    for i in s :
        if i == '[' :
            pass
        elif i in  [',',']'] :
            nums.append(a)
            a = ''
        else :
            a += i
    r = False
    error = False
    for i in p :
        if i == 'R' : # R이 나오면 실제 뒤집는게 아닌 pop방향을 바꿔준다.
            r = not r
        else :
            if n > 0:
                if not r :
                    nums.popleft()
                    n -= 1
                else :
                    nums.pop()
                    n -= 1
            elif n == 0 : 
                error = True
                break
    if error :
        print('error')
    else :
        if r :
            nums = list(nums)[::-1]
        print('[', end='')
        for i in range(n) :
            if i == n-1 :
                print(nums[i], end='')
            else :
                print(nums[i],',', sep='', end='')
        print(']')


