# 17425  약수의 합 G4

from itertools import accumulate
import sys


def solution() :
    input = sys.stdin.readline
    M = 1000001
    nums = [1]*M
    for i in range(2, M) :
        for j in range(i, M, i) :
            nums[j] += i
    nums[0] = 0
    nums = list(accumulate(nums))
    T = int(input())
    answers = [0]*T
    for t in range(T) :
        N = int(input())
        answers[t] = nums[N]
    return answers

if __name__ == "__main__" :
    print(*solution(), sep='\n')