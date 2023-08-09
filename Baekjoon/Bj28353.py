# 28353 고양이 카페 S3

def solution() :
    N, K = map(int, input().split())
    nums = list(map(int, input().split()))
    nums.sort()
    s, e = 0, N-1
    ans = 0
    while s < e :
        if nums[s] + nums[e] > K :
            e -= 1
        else :
            ans += 1
            s += 1
            e -= 1
    return ans

if __name__ == "__main__" :
    print(solution())