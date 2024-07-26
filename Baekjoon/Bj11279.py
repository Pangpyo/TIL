# 11279 최대 힙 S2

from heapq import heappop, heappush
import sys


def solution():
    input = sys.stdin.readline
    N = int(input())
    answer = []
    heap = []
    for _ in range(N):
        x = int(input())
        if x:
            heappush(heap, -x)
        else:
            if heap:
                answer.append(-heappop(heap))
            else:
                answer.append(0)
    return answer

if __name__ == "__main__":
    print(*solution(), sep='\n')