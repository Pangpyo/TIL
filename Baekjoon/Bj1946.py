# 1946 신입사원 S1

import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline # N이 10만 이상으로 매우 커질 수 있으므로 표준입력을 받음

for _ in range(int(input().rstrip())) : # 표준입력을 받을시 개행문자가 붙으므로 제거해줌
    N = int(input().rstrip())
    p = [] # 회사원들의 성적 기록
    for i in range(N) :
        a, b = map(int, input().split())
        p.append((a, b))
    p = sorted(p) # sorted로 정렬해줌. 이 경우에는 a를 기준으로 정렬됨
    new = 1 # a를 기준으로 1등인 사람은 반드시 합격한다. 그러므로 새 신입사원 수는 1부터 시작
    tmp = p[0][1] # a가 1등인 사원의 b등수를 저장
    for i in range(1, N) : # a가 2등일때부터 검사해줌
        if tmp > p[i][1] : # 검사하는 사원의 b등수가 저장된 등수보다 높을 시 합격
            new += 1    # 합격자 + 1
            tmp = p[i][1] # 합격 하한 등수 최신화
    print(new) # 총 합격자 수 출력