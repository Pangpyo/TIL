# 21758 꿀 따기 G5

from itertools import accumulate


def solution() :
    N = int(input())
    nums = list(map(int, input().split()))
    D = list(accumulate(nums))
    answer = 0
    for i in range(1, N-1) :
        start = D[N-1] * 2 - D[0] - D[i] - nums[i]
        mid = D[N-2] + nums[i] - D[0] 
        end = D[N-1] + D[i-1] - nums[N-1] - nums[i]
        answer = max(answer, start, mid, end)
    return answer

if __name__ == "__main__" :
    print(solution())
