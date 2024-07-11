# 3372 보드 점프 S1

import sys


def solution():
    input = sys.stdin.readline
    N = int(input())
    board = tuple(tuple(map(int, input().split())) for _ in range(N))
    D = [[0]*N for _ in range(N)]
    D[0][0] = 1
    for x in range(N):
        for y in range(N):
            b = board[x][y]
            if b == 0:
                continue
            nx = x + b
            ny = y + b
            if nx < N:
                D[nx][y] += D[x][y]
            if ny < N:
                D[x][ny] += D[x][y]
    return D[-1][-1]

if __name__ == "__main__":
    print(solution())