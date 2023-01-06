# 1961 숫자 배열 회전 D2


def rotate(n, B: list):
    nB = []
    for i in range(n):
        temp = [B[j][i] for j in range(n - 1, -1, -1)]
        nB.append(temp)
    return nB


for t in range(1, int(input()) + 1):
    n = int(input())
    board = [list(input().split()) for _ in range(n)]
    board1 = rotate(n, board)
    board2 = rotate(n, board1)
    board3 = rotate(n, board2)
    print(f"#{t}")
    for i in range(n):
        print(*board1[i], sep="", end=" ")
        print(*board2[i], sep="", end=" ")
        print(*board3[i], sep="")
