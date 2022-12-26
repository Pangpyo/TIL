# 3190 뱀 G4

from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
board = [[0] * N for _ in range(N)]  # 뱀이 이동할 보드

K = int(input())

for _ in range(K):
    a, b = map(int, input().split())  # 사과를 보드에 놓아준다
    board[a - 1][b - 1] = 2

dx = [0, 1, 0, -1]  # 방향전환을 위한 리스트
dy = [1, 0, -1, 0]


L = int(input())
snake = [tuple(input().split()) for _ in range(L)]  # 뱀의 이동정보
snake.append((10000, ""))  # 마지막에는 쭉 직진


def game():
    x = 0  # 뱀의 x좌표
    y = 0  # 뱀의 y좌표
    s = 0  # 시간
    d = 0  # 방향
    tail = deque([(x, y)])  # 뱀이 지나간 자리를 큐로 저장한다
    board[x][y] = 1  # 시작한 자리를 1로 바꿔준다
    for t, C in snake:
        t = int(t)
        for _ in range(t - s):  # 입력이 들어온 시간에서 현재 시간을 뺀 만큼 이동한다
            x += dx[d]  # 지금 머리가 향해있는 방향으로
            y += dy[d]
            if (
                x >= N or x < 0 or y >= N or y < 0 or board[x][y] == 1
            ):  # 머리가 몸통을 밟거나 보드 밖으로 빠져나가는경우
                return s + 1  # 종료하고 시간을 return한다
            if board[x][y] == 2:  # 사과를 먹은 경우 몸이 한칸 늘어난다
                pass
            else:  # 사과를 먹지 않은 경우 꼬리가 한칸 따라온다
                a, b = tail.popleft()  # 꼬리에서 한칸 pop해주고
                board[a][b] = 0  # 그 좌표를 0으로 되돌려준다
            board[x][y] = 1  # 머리가 한칸 나아간다
            tail.append((x, y))  # 머리가 나아간 자리를 tail에 더해준다
            s += 1  # 시간 += 1

        if C == "D":  # D인경우 방향을 오른쪽으로 바꿔준다
            d = (d + 1) % 4
        elif C == "L":  # L인 경우 방향을 왼쪽으로 바꿔준다
            d = (d - 1) % 4
    return s  # 모든 시간이 지나고도 return되지 않았을 경우 최종 시간을 return


print(game())
