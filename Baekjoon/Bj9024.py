# 9024 두 수의 합 G5

import sys

def solution() :
    input = sys.stdin.readline
    T = int(input())
    ans = [0]*T
    for t in range(T) :
        N, K = map(int, input().split())
        nums = list(map(int, input().split()))
        nums.sort()
        coms = []
        s, e = 0, N-1
        diff = sys.maxsize
        while s < e :
            su = nums[s] + nums[e]
            if abs(K-su) <= diff :
                coms.append((abs(K-su), nums[s], nums[e]))
            if su <= K :
                s += 1
            else :
                e -= 1
        coms.sort(key=lambda x : x[0])
        minV = coms[0][0]
        for com in coms :
            if com[0] == minV :
                ans[t] += 1
    return ans

if __name__ == "__main__" :
    print(*solution(), sep="\n")