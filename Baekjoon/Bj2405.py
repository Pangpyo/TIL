# 2405 세 수, 두 M G4

import sys

def solution() :
    input = sys.stdin.readline
    n = int(input())
    nums = [int(input()) for _ in range(n)]
    nums.sort()
    answer = 0
    for i in range(1, n-1) :
        answer = max(answer, abs(nums[i-1] - nums[i]*2 + nums[-1]), abs(nums[0] - nums[i]*2 + nums[i+1]))
    return answer


if __name__ == "__main__" :
    print(solution())