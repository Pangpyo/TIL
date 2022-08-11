# 2979 트럭주차 B2

import sys


sys.stdin = open('input.txt')

A, B, C = map(int, input().split())

time = [0]*101

for _ in range(3) :
    t1, t2 = map(int, input().split())
    for i in range(t1, t2) :
        time[i] += 1
print(time.count(1)*A + time.count(2)*B*2 + time.count(3)*C*3)