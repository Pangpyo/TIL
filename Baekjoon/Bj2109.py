# 2109 순회강연 G3

from collections import deque
import heapq
import sys


input = sys.stdin.readline

n = int(input())

U = sorted(
    list(tuple(map(int, input().split())) for _ in range(n)),
    key=lambda x: (-x[1], x[0]),
)

U = deque(U)
U.append((0, 0))


def answer():
    H = []
    A = []
    while U:
        p, d = U.popleft()
        while H and day > d:
            heapq.heappush(A, -heapq.heappop(H))
            day -= 1
        heapq.heappush(H, -p)
        day = d
    return sum(A)


print(answer())
