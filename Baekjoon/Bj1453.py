# 1453 피시방 알바 B2

import sys

sys.stdin = open('input.txt')

N = int(input())

seatnum = set(map(int, input().split())) # set를 사용해 중복 제거

print(N-len(seatnum))