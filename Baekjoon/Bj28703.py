# 28703 Double it G3

from heapq import heapify, heappop, heappush

def solution() :
    N = int(input())
    nums = list(map(int, input().split()))
    heapify(nums)
    twos = tuple((1<<i) for i in range(32))
    max_n = max(nums)
    answer = max_n - nums[0]
    cnt = 0
    while True :
        n = heappop(nums) * 2
        heappush(nums, n)
        max_n = max(max_n, n)
        temp = max_n-nums[0]
        if temp > answer :
            cnt += 1
            if cnt >= N :
                break
        else :
            cnt = 0
        answer = min(answer, temp)
    return answer

if __name__ == "__main__" :
    print(solution())