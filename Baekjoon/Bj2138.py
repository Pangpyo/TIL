# 2138 전구와 스위치 G5
from copy import deepcopy


N = int(input())
A = list(map(int, (list(input()))))
B = list(map(int, (list(input()))))
A_ = deepcopy(A)


def swich(n):
    for i in [-1, 0, 1]:
        if 0 <= n + i < N:
            A[n + i] = (A[n + i] + 1) % 2


def solution():
    cnt = 0
    for i in range(1, N):
        if A[i - 1] != B[i - 1]:
            swich(i)
            cnt += 1
    if A == B:
        return cnt
    return float("inf")


ans = solution()

A = A_
swich(0)


ans = min(ans, solution() + 1)

print(ans if ans != float("inf") else -1)
