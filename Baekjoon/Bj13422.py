# 13422 도둑 G4

from itertools import accumulate
import sys


def solution():
    input = sys.stdin.readline
    T = int(input())
    answers = [0]*T
    for t in range(T):
        N, M, K = map(int, input().split())
        nums = tuple(map(int, input().split()))*2
        nums = tuple(accumulate(nums))
        answer = 0
        if N == M:
            answer = 1 if nums[N-1] < K else 0
        else:
            for i in range(M, N+M):
                if nums[i]-nums[i-M] < K:
                    answer += 1
        answers[t] = answer
    return answers

if __name__ == "__main__":
    print(*solution(), sep='\n')