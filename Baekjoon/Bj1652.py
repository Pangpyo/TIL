# 1652 누울자리 B1

import sys


sys.stdin = open('input.txt')

N = int(input())

room = [list(input()) for _ in range(N)] # 방의 모양
row = 0 # 각 행의 누을 자리의 개수
col = 0 # 각 열의 누울 자리의 개수
for i in range(N) : # 각 행의 누울 자리 탐색
    empty = 0 # 빈 칸
    for j in range(N) :
        if room[i][j] == '.' : # '.'이 나올 경우 빈 칸이 1칸 늘었다고 저장해줌
            empty += 1
        else : # 짐이 나올 경우 빈 칸을 다시 0으로 만들어줌
            empty = 0
        if empty == 2 : # 빈 칸이 두 칸 이상일 경우 누울 자리의 개수를 1개 늘려줌
            row += 1

for i in range(N) : #열에 대해서도 같은 작업 반복
    empty = 0 
    for j in range(N) :
        if room[j][i] == '.' :
            empty += 1
        else :
            empty = 0
        if empty == 2 :
            col += 1
    
print(row, col)