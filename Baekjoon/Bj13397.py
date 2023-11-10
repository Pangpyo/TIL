# 13397 구간 나누리 2 G4

def solution() :
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    s, e = 0, max(nums)
    ans = e
    while s <= e :
        mid = (s+e)//2
        min_temp = nums[0]
        max_temp = nums[0]
        m = 1
        for n in nums :
            if max(n-min_temp, max_temp-n) > mid:
                m += 1
                min_temp = n
                max_temp = n
            else :
                min_temp = min(min_temp, n)
                max_temp = max(max_temp, n)
        if m <= M :
            e = mid - 1
            ans = min(ans, mid)
        else :
            s = mid + 1

    return ans

if __name__ == "__main__" :
    print(solution())