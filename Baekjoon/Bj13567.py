# 13567 로봇 S4

import sys

sys.stdin = open('input.txt')

M, n = map(int, input().split())
x = 0
y = 0
i = 0
fail = 0
for _ in range(n) :
    dx = [1, 0, -1, 0] # 오른쪽, 위쪽, 왼쪽, 아래쪽
    dy = [0, 1, 0, -1]
    MT , d = input().split()
    d = int(d)
    if MT == 'MOVE' : # MOVE일시 해당 방향으로 d만큼 이동
        x += dx[i]*d
        y += dy[i]*d
    else : # TURN일 경우 
        if d == 0 : # d가 0이면 왼쪽으로 방향 전환
            i = (i+1)%4
        else : # d가 1이면 오른쪽으로 방향 전환
            i = (i-1)%4
    if x < 0 or x > M or y < 0 or y > M : # 체스판의 바깥으로 넘어갈 경우 실패
        fail = 1
if fail == 0 : # 실패하지 않을 경우 좌표 출력
    print(x, y)
else : # 실패 할 경우 -1
    print(-1)