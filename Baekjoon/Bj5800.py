# 5800 성적 통계 S5

import sys


sys.stdin = open('input.txt')

K = int(input())

for i in range(1, K+1) :
    score = list(map(int, input().split()))
    N = score.pop(0)
    score.sort(reverse=True) # 내림차순 정렬
    maxgap = 0
    for j in range(1, N) :
        gap = score[j-1] - score[j] # 인접한 두 점수의 차이
        maxgap = gap if gap > maxgap else maxgap #가장 큰 차이를 저장
    print(f'Class {i}\nMax {max(score)}, Min {min(score)}, Largest gap {maxgap}')


