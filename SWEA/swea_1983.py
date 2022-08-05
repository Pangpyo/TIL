# 1983 조교의 성적 매기기 D2

import sys

sys.stdin = open("_조교의성적매기기.txt")

T = int(input())

for i in range(1, T+1) :
    N, K = map(int, input().split())
    students = {}
    for j in range(1, N+1) :
        mid, final, assin = list(map(int, input().split())) # 중간고사, 기말고사, 과제 점수를 입력받는다
        score = mid*0.35 + final*0.45 +assin*0.20 # 중간고사, 기말고사, 과제점수를 비중에 맞게 총 점수를 계산한다.
        students[j] = score # 학생번호 : 점수의 딕셔너리를 만든다.
    students = sorted(students.items(), key = lambda x : -x[1]) # 딕셔너리를 점수의 내림차순으로 정렬한다.
    rank = 0 # 등수를 저장할 변수를 만든다. ( 0등이 1등이다.)
    for k,v in students :
        if k == K : # 내가 찾는 학생이 몇 등에 있는지 확인한다.
            break
        rank += 1
    grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0'] # 평점을 리스트로 만들었다.

    ans = grade[int((rank)//(N/10))] 
    # 등급은 총 10가지이므로 (총 학생수/10)으로 등수를 나눈 몫을 평점 리스트에 대입하면 평점이 나온다.
    print('#%d'%i, ans)