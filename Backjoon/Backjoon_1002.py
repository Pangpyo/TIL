# 1002번 터렛 S3

import sys

sys.stdin = open("input.txt", "r")

from math import sqrt

T = int(input())

for i in range(1, T+1) :
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = sqrt((x1-x2)**2+(y1-y2)**2)
    if d == 0 : # 원의 중심이 같은 경우
        if r1 == r2 : #반지름이 같은 경우
            print(-1)
        else : 
            print(0)
    elif d < r1 or d < r2 :  # 내접할 경우
        if d == abs(r1-r2) : # 한 점에서 만날 경우
            print(1)
        elif d < abs(r1-r2) : # 만나지 않을 경우
            print(0)
        elif d > abs(r1-r2) : # 두 점에서 만날 경우
            print(2)
    else : #외접할 경우
        if d == (r1+r2) : # 한 점에서 만날 경우
            print(1)
        elif d < (r1+r2) : # 두 점에서 만날 경우
            print(2)
        elif d > (r1+r2) : # 만나지 않을 경우
            print(0)
    