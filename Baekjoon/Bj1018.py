# 1018 체스판 다시 칠하기 S4

import sys


sys.stdin = open('input.txt')

N, M = map(int, input().split())

board = [list(input()) for _ in range(N)]

def WB(x, y, color1, color2) : # 자르기 시작할 좌표와 칠할 색을 순서대로 입력해줌
    ans = 0
    for nx in range(x, x+8) :
        for ny in range(y, y+8) :
            if (nx+ny)%2 == 0 and board[nx][ny] != color1 : # 입력한 색의 순서와 맞지 않은 색일경우
                ans += 1 # 칠한 횟수에 +1
            elif (nx+ny)%2 == 1 and board[nx][ny] != color2 : # 홀수칸에도 동일한 작업
                ans += 1
    return ans
paint = 64 # 칠해야 하는 정사각형 갯수의 최댓값
for i in range(N-7) : 
    for j in range(M-7) : # 만들 수 있는 8*8 체스판의 모든 경우를 검사
        W = WB(i, j, 'W', 'B') 
        B = WB(i, j, 'B', 'W')
        paint = min(W, B) if min(W, B) < paint else paint
print(paint)

