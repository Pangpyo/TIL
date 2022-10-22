# 10942 팰린드롬? G4

from pprint import pprint
import sys


sys.stdin = open("input.txt")
# input = sys.stdin.readline
N = int(input())


nums = list(map(int, input().split()))
D = [[0] * N for i in range(N)]

for i in range(N):
    D[i][i] = 1

for i in range(1, N):
    if nums[i] == nums[i - 1]:
        if i - 1 < 0:
            continue
        D[i][i - 1] = 1
    for j in range(N):
        if D[i - 1][j] and nums[j - 1] == nums[i]:
            D[i][j - 1] = 1


M = int(input())


for i in range(M):
    S, E = map(int, input().split())
    if D[E - 1][S - 1]:
        print(1)
    else:
        print(0)
