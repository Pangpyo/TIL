# 2374 같은 수로 만들기 G4

import sys


def solution() :
    input = sys.stdin.readline
    n = int(input())
    nums = []
    for _ in range(n) :
        a = int(input())
        if not nums or nums[-1] != a :
            nums.append(a)
    high, now = nums[0], nums[0]
    answer = 0
    for a in nums :
        if a > high :
            answer += a - high
            high = a
        if a < now :
            answer += now - a
        now = a
    return answer
if __name__ == "__main__" : 
    print(solution())