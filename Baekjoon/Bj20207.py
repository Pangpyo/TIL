# 20207 달력 G5

import sys
from heapq import heappop, heappush
def solution() :
    input = sys.stdin.readline
    N = int(input())
    days = [tuple(map(int, input().split())) for _ in range(N)]
    days.sort()
    answer = 0
    heap = [-1]
    ps = 0
    for s, e in days :
        mh = max(heap)
        if s > mh+1 :
            answer += len(heap) * (mh-ps+1)
            heap = []
            ps = s
        if not heap or heap[0] >= s  :
            heappush(heap, e)
        else :
            heappop(heap)
            heappush(heap, e)

    answer += len(heap) * (max(heap)-ps+1)
    return answer

if __name__ == "__main__" :
    print(solution())