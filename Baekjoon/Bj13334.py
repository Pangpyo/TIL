# 13334 철로 G2

from heapq import heappop, heappush
import sys


def solution() :
    input = sys.stdin.readline
    N = int(input())
    starts = []
    inside = []
    lines = []
    for _ in range(N) :
        a, b = map(int, input().split())
        starts.append(min(a, b))
        heappush(lines, (max(a, b), min(a, b)))
    l = int(input())
    answer = 0
    starts.sort()
    for start in starts :
        while inside and inside[0] < start :
            heappop(inside)
        while lines and lines[0][0] <= start + l :
            e, s = heappop(lines)
            if s >= start :
                heappush(inside, s)
        answer = max(answer, len(inside))
    return answer

if __name__ == "__main__" :
    print(solution())