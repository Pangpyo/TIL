# 2063. 중간값 찾기 D1

import sys


sys.stdin = open('input.txt')

N = int(input())

score = sorted(list(map(int, input().split())))
print(score[int((N-1)/2)])