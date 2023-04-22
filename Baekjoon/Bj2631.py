# 2631 줄세우기
from bisect import bisect_left as bl
import sys


def solution():
    input = sys.stdin.readline
    N = int(input())
    D = [int(input())]
    for i in range(1, N):
        n = int(input())
        if n > D[-1]:
            D.append(n)
        else:
            D[bl(D, n)] = n
    return N - len(D)


if __name__ == "__main__":
    print(solution())
