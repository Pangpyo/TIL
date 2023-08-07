# 21773 가희와 프로세스1 G5

import sys
from heapq import heappop, heappush

def solution() :
    input = sys.stdin.readline
    T, n = map(int, input().split())
    heap = []
    for i in range(n) :
        a, b, c = map(int, input().split())
        heappush(heap, (-c, a, b))
    ans = []
    idx = 0
    while heap and idx < T:
        a, b, c = heappop(heap)
        ans.append(b)
        idx += 1
        if c == 1 :
            continue
        heappush(heap, (a +1, b, c-1))
    return ans

if __name__ == "__main__" :
    print(*solution(), sep="\n")