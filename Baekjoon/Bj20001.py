# 20001 고무오리 디버깅 B1

import sys


sys.stdin = open('input.txt')

start = input()
prob = 0
while 1 :
    duck = input()
    if duck == '문제' :
        prob += 1
    elif duck == '고무오리' :
        if prob == 0 :
            prob += 2
        else :
            prob -= 1
    else :
        break

print('고무오리야 사랑해' if prob == 0 else '힝구')