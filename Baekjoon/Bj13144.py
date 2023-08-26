# 13144 List of Unique Numbers G4

def solution() :
    N = int(input())
    nums = list(map(int, input().split()))
    dic = {}
    pre = -1
    ans = 0
    for i in range(N) :
        if nums[i] in dic :
           pre = max(pre, dic[nums[i]])
        dic[nums[i]] = i
        ans += i - pre
    return ans

if __name__ == "__main__" :
    print(solution())