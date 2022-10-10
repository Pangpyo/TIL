# 17503 맥주 축제 S2

from collections import deque
import heapq
import sys


input = sys.stdin.readline

sys.stdin = open("input.txt")

N, M, K = map(int, input().split())
beer = []
for i in range(K):
    v, c = map(int, input().split())
    beer.append((c, v))
beer.sort()
beer = deque(beer)


def solution(N, M, beer: deque):
    liver = 0
    drink = []
    total = 0
    while beer:
        c, v = beer.popleft()
        if len(drink) < N:
            heapq.heappush(drink, v)
            total += v
        else:
            total -= heapq.heappop(drink)
            heapq.heappush(drink, v)
            total += v
        if total >= M and len(drink) == N:
            liver = c
            break
    if total >= M:
        return liver
    else:
        return -1


print(solution(N, M, beer))
