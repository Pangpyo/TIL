# 2897 몬스터 트럭 B1

import sys

sys.stdin = open("input.txt")

R, C = map(int, input().split())


carpark = [list(input()) for _ in range(R)]
dx = [0, 0, 1, 1]
dy = [0, 1, 0, 1] # 현 위치, 오른쪽, 아래, 오른쪽 아래 검사
spot = [0]*5 # 각 인덱스 위치가 부서진 차의 개수와 매칭됨
for x in range(R) :
    for y in range(C) :
        broken = 0 # 부서진 차의 개수
        place = 0 # 주차 할 수 있는 공간
        for i in range(4) : 
            nx = x + dx[i] # 
            ny = y + dy[i]
            if nx < R and ny < C :
                if carpark[nx][ny] == '.' :
                    place += 1
                elif carpark[nx][ny] == 'X' :
                    place += 1
                    broken +=1
                else : 
                    break
        if place == 4 : # 주차 공간이 나온다면
            spot[broken] += 1 # 부순 차의 개수가 들어가는 인덱스에 +1을 해줌
print(*spot, sep= '\n')

