# 11501 주식 S2

import sys

def solution() :
    input = sys.stdin.readline
    T = int(input())
    answers = [0]*T
    for t in range(T) :
        N = int(input())
        nums = list(map(int, input().split())) 
        ans = 0
        sell = nums[-1]
        for i in reversed(range(N-1)) :
            if nums[i] < sell :
                ans += sell-nums[i]
            else :
                sell = nums[i]
        answers[t] = ans
    return answers

if __name__ == "__main__" :
    print(*solution(), sep="\n")