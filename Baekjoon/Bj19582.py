# 19582 200년간 폐관수련했더니 PS 최강자가 된 건에 대하여 G3


import sys
from heapq import heappush, heappop


def solution():
    input = sys.stdin.readline
    N = int(input())
    heap = []
    money = 0
    for _ in range(N):
        x, y = map(int, input().split())
        if money <= x:
            heappush(heap, -y)
            money += y
        else:
            if -heap[0] > y and money + heap[0] <= x:
                money += heappop(heap) + y
                heappush(heap, -y)

    if len(heap) >= N - 1:
        return "Kkeo-eok"
    else:
        return "Zzz"


if __name__ == "__main__":
    print(solution())
