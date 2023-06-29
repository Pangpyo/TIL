# 23254 나는 기말고사형 인간이야 G5

from heapq import heappop, heappush
import sys


def solution() :
    input = sys.stdin.readline
    N, M = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    heap = []
    time = N*24
    for i in range(M) :
        heappush(heap, (-b[i], 100-a[i]))
    ans = sum(a)
    while heap and time:
        point, total = heappop(heap)
        point *= -1
        temp = total//point
        used = min(time, temp)
        total -= used*point
        ans += used*point
        time -= used
        if total :
            heappush(heap, (-total, total))
    return ans

if __name__ == "__main__" :
    print(solution())