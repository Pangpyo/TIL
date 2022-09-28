# 2002 추월 S1

import sys


input = sys.stdin.readline  # 입력 수가 많으므로 표준입력

N = int(input())
car_in = {}  # 들어오는 차
car_out = {}  # 나가는 차
for i in range(N):
    car_in[input().rstrip()] = i  # 개행문자 제거
for i in range(N):
    car_out[input().rstrip()] = i

car_in = list(car_in.items())  # 들어오는차를 items로 만들어줌
cnt = 0
for i in range(1, N):
    k, v = car_in[i]  # 앞쪽부터 순서대로 차 검사
    for j in range(0, i):
        k_pre, v_pre = car_in[j]  # 검사하는 차가 들어올때 앞에 있던 차들 중 단 하나라도 나갈 때 뒤에 있을 경우
        if car_out[k] <= car_out[k_pre]:
            cnt += 1  # 추월로 판정
            break  # 다음 차 검사
print(cnt)
