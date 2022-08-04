# 9455 박스 B1

import sys

sys.stdin = open('input.txt')

T = int(input())

for _ in range(T) :
    m, n = map(int, input().split())
    room = [list(map(int, input().split())) for _ in range(m)]
    box = 0 # 박스의 이동횟수 저장
    for _ in range(m) : #행의 개수만큼 반복
        for i in range(m-2, -1, -1) : # 끝에서 2번째 행부터 박스를 움직임
            for j in range(n) :
                if room[i][j] == 1 and room[i+1][j] == 0 : # 아래로 한 칸 움직일수 있을 경우
                    room[i][j] = 0 
                    room[i+1][j] = 1 # 박스를 아래로 한 칸 움직임
                    box += 1 # 박스의 이동횟수 +1
    print(box)
        