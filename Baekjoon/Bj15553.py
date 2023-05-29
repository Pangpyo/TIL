# 15553 난로 G5

import sys


def solution() :
    input = sys.stdin.readline
    N, K = map(int, input().split())
    nums = [int(input()) for _ in range(N)]
    terms = []
    for i in range(1, N) :
        terms.append(nums[i]-nums[i-1]-1)
    terms.sort(reverse=True)
    total = nums[-1]-nums[0] +1
    total -= sum(terms[0:K-1])
    
    return total
if __name__ == "__main__" :
    print(solution())