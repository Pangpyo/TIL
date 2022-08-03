# 5533 유니크 B1

import sys

sys.stdin = open('input.txt')

N = int(input()) 


num = [list(map(int, input().split())) for _ in range(N)]
# 2차원 리스트로 만들어준다.
score = [0]*N # 각 참가자의 점수를 저장할 리스트를 만들어준다.
for j in range(3) : #열은 3개로 고정
    for i in range(N) : # 0
        if [k[j] for k in num].count(num[i][j]) == 1 : 
#열을 따로 뽑아내 그 안에 있는 중복되는 숫자를 세어준다.
            score[i] += num[i][j]
print(*score, sep = '\n')