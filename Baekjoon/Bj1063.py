# 1063 킹 S3

import sys

sys.stdin = open('input.txt')
board = [[0]*8 for _ in range(8)]
king, piece, N = input().split()
x = -int(king[1])
y = ord(king[0])-65
x1 = -int(piece[1])
y1 = ord(piece[0])-65
board[x][y] = 1
board[x1][y1] = 2


word = ['R', 'L', 'B', 'T', 'RT', 'LT', 'RB', 'LB']
dx = [0, 0, 1, -1, -1, -1, 1, 1]
dy = [1, -1, 0, 0, 1, -1, 1, -1]

for i in range(int(N)) :
    a = input() # 명령어 받아줌
    for i in range(8) : # 8방위 탐색
        if a == word[i] : # 해당 방향으로 이동 시작
            if -8 <= x+dx[i] <= -1 and 0 <= y+dy[i] <= 7: 
                if board[x+dx[i]][y+dy[i]] == 0 :
                    board[x][y] = 0
                    board[x+dx[i]][y+dy[i]] = 1
                    x = x+dx[i]
                    y = y+dy[i]
                elif board[x+dx[i]][y+dy[i]] == 2 and -8 <= x1+dx[i] <= -1 and 0 <= y1+dy[i] <= 7:
                    board[x][y] = 0
                    board[x+dx[i]][y+dy[i]] = 1 #킹을 움직임
                    board[x+2*dx[i]][y+2*dy[i]] = 2 #돌도 한칸 움직임
                    x = x+dx[i]
                    y = y+dy[i]
                    x1 = x1+dx[i]
                    y1 = y1+dy[i]
print(chr(y+65), -x, sep = '') #킹의 좌표
print(chr(y1+65), -x1, sep = '') #돌의 좌표


