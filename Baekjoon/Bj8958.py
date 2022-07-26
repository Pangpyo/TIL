# 8958 OX퀴즈 B2
import sys

sys.stdin = open("3_OX퀴즈.txt")

T = int(input())

for i in range(1, T+1) :
    OX = input() 
    score = 1 #기본점수는 1점
    total = 0 #얻은 점수를 저장할 변수
    for ox in OX : #for문을 통해 인덱스를 하나씩 검사
        if ox == 'O' : #'O'일 경우 총합에 스코어를 더해주고, 스코어도 1점 올라감
            total += score 
            score += 1
        else : #'X'일경우 스코어를 다시 1로 초기화
            score = 1
    print(total)