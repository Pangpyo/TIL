# 2615 오목 S2


import sys

sys.stdin = open('input.txt')

board = [[-1]+list(map(int, input().split()))+[-1] for _ in range(19)]
line = [-1]*21
board.insert(0, line)
board.append(line)
# 오목판을 리스트로 받으며, 인덱스 초과를 해결하기 위해 주변에 테두리를 둘러줌.

def omok(board, x, y) :
    ans = 0
    dx = [1, 1, 0, -1]
    dy = [0, 1, 1, 1] # 아래, 오른쪽 아래, 오른쪽, 오른쪽 위
    if board[x][y] : # 검사하는 칸이 빈 칸이 아닐 경우
        color = board[x][y]  # 해당 돌의 색 을 변수로 지정
        for i in range(4) : # 4방향으로 검사
            nx = x 
            ny = y # 방향을 이동하면서 변화할 값 nx, ny 지정
            go = 1 # 같은 색의 연속된 바둑알의 개수
            if board[nx-dx[i]][ny-dy[i]] != color :
            # 현재 검사하는 방향의 바로 전 칸이 같은 돌일 경우에는 검사 할 필요가 없으므로 아닐 경우면 검사
                for _ in range(6) : # 육목까지 생각해 최대 6개의 돌만 검사하면 된다.
                    nx += dx[i]
                    ny += dy[i]
                    if board[nx][ny] == color :
                        go += 1 # 한 방향으로 같은 바둑알이 연속으로 있을 경우 +1
                        if go == 5 : # 오목이 완성된 경우 결과값에 해당 색 출력
                            ans = color
                        if go == 6 : # 6목까지 간 경우 다시 ans를 0으로 반환
                            ans = 0
                    else :
                        break
    return ans

for x in range(1, 20) :
    for y in range(1, 20) :
        win= omok(board, x, y)
        if win != 0 :
            print(win)
            print(x, y)
            exit(0)
print(0) # 모든 판을 검사 한 후에도 승리 조건을 채우지 못할 경우, 0출력

#     dx = [-1, 0, 1, 1] 
#     dy = [1, 1, 0, 1] 검사 순서를 이렇게 작성 했을때는 오답이 났다. 이유가 뭘까?


            
            
