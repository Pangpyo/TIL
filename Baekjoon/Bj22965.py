# 22965 k개의 부분 배열 G4

from collections import defaultdict


def solution():
    N = int(input())
    nums = list(map(int, input().split()))
    now = -1
    cnt = 0
    sorted_nums = sorted(nums)
    dic = defaultdict(int)
    for i, n in enumerate(sorted_nums):
        dic[n] = i
    dic[-1] = -float('inf')
    for n in nums:
        if dic[n] != dic[now]+1:
            cnt += 1
        now = n
    return cnt if cnt < 3 else 3

if __name__ == "__main__":
    print(solution())