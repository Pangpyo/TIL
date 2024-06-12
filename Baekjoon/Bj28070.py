# 28070 유니의 편지 쓰기 G5

from itertools import accumulate
import sys


def solution():
    input = sys.stdin.readline
    N = int(input())
    date = set()
    periods = []
    for _ in range(N):
        s, e = input().split()
        date.add(s)
        date.add(e)
        periods.append((s, e))
    date = list(date)
    date.sort()
    dic = {}
    for i, d in enumerate(date):
        dic[d] = i
    prefix_sum = [0]*(len(date)+2)
    for s, e in periods:
        prefix_sum[dic[s]] += 1
        prefix_sum[dic[e] + 1] -= 1
    prefix_sum = tuple(accumulate(prefix_sum))
    answer = ''
    cnt = -1
    for i, n in enumerate(prefix_sum):
        if i == len(date):
            break
        if n > cnt:
            cnt = n
            answer = date[i]
    return answer

if __name__ == "__main__":
    print(solution())