# 1236 성 지키기 B1
import sys

sys.stdin = open('input.txt')

N, M = map(int, input().split()) # 행과 열을 입력받는다

castle = [list(input()) for _ in range(N)] # 성의 병사 위치를 입력받는다

secur_1 = 0 # 각 행에 필요한 경비의 수 

for i in range(N) :
    if 'X' not in castle[i] : # X가 없으면
        secur_1 += 1 # 변수에 +1
secur_2 = 0 # 각 열에 필요한 경비의 수 
for i in range(M) : # 0
    if 'X' not in [j[i] for j in castle]: # [castle[0][0], castle[1][0]...]
        secur_2 += 1

print(secur_1 if secur_1>secur_2 else secur_2) 
# 행에 필요한 경비와 열에 필요한 경비의 수중 많은 것을 출력

