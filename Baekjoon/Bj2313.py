# 2313 보석 구매하기 G5

import sys


def solution():
    input = sys.stdin.readline
    N = int(input())
    answer = [0]
    for n in range(N):
        L = int(input())
        nums = tuple(map(int, input().split()))
        pre = 0
        cost = -sys.maxsize
        temp = 0
        s, e = 0, 0
        for i, num in enumerate(nums):
            temp += num
            if temp > cost or (temp == cost and e-s > i-pre):
                s = pre + 1
                e = i + 1
                cost = temp
            if temp <= 0:
                pre = i + 1
                temp = 0
        answer[0] += cost
        answer.append(f'{s} {e}')
    return answer

if __name__ == "__main__":
    print(*solution(), sep='\n')