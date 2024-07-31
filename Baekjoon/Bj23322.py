# 23322 초콜릿 뻇어 먹기 S2

from collections import deque
import sys


def solution():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    A = deque(sorted(list(map(int, input().split()))))
    c, d = 0, 0
    while True:
        a = A.pop()
        if a > A[0]:
            c += a - A[0]
            d += 1
            A.appendleft(A[0])
        else:
            break
    return c, d

if __name__ == "__main__":
    print(*solution())