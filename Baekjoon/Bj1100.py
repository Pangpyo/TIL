# 1100 하얀 칸 B2

import sys

sys.stdin = open('input.txt')

chess = [list(input()) for _ in range(8)] 
# 체스판의 상태를 2차원 리스트로 입력받는다.
pieces_white = 0 # 하얀 칸의 말들을 세어줄 변수를 지정해준다.
for i in range(8) : # 각 행을 검사
    for j in range(8) : # 각 열을 검사
        if (i+j)%2 == 0 and chess[i][j] == 'F' : 
# 행과 열의 합이 짝수일 때 하얀 판이다. 그 하얀 판에 'F'가 있을 시 세어준다.
            pieces_white += 1
print(pieces_white)