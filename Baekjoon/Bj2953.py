# 2953 나는 요리사다 B3

import sys

sys.stdin = open("input.txt")
score = [] # 각 참가자의 총 점수를 저장할 리스트 생성
for i in range(5) : #5줄의 입력을 받음
    score.append(sum(list(map(int, input().split())))) # 입력받은 줄의 총 합을 저장

print(score.index(max(score))+1, max(score)) 
# 점수중 가장 높은 값과 그 값의 인덱스를 출력, 인덱스는 1을 더해서 참가자 번호에 맞춰줌
