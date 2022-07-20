# 1204. [S/W 문제해결 기본] 1일차 - 최빈수 구하기 D2

import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for i in range(1, T+1) :
    n = int(input())
    score = list(map(int, input().split()))
    score_count = []
    for i in range(0,101) :
        score_count.append(score.count(i))
    max_s = score_count[::-1].index(max(score_count)) # 최빈수가 가장 여러개일 때 가장 큰 값을 찾기 위해 뒤에서부터 찾아줬음.
    print('#%d'%n, len(score_count)-max_s-1)