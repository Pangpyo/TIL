# 18114 블랙 프라이데이 G5

from bisect import bisect_left as bl


def solution() :
    N, C = map(int, input().split())
    nums = list(map(int, input().split()))
    nums.sort()
    for i in range(N) :
        if nums[i] == C :
            return 1
        for j in range(i) :
            if nums[i]+nums[j] == C :
                return 1
            temp = bl(nums, C-(nums[i]+nums[j]), i+1)
            if temp >= N :
                continue
            if nums[i]+nums[j]+nums[temp] == C:
                return 1
    return 0

if __name__=="__main__" :
    print(solution())