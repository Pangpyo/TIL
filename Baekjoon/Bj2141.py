# 2141 우체국 G4

import sys

input = sys.stdin.readline

N = int(input())
XA = []
total = 0
for i in range(N):
    XA.append(tuple(map(int, input().split())))
    total += XA[-1][1]

XA.sort()

temp = 0
for i in range(N):
    temp += XA[i][1]
    if temp >= (total + 1) // 2:
        print(XA[i][0])
        break
