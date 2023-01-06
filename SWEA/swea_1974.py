# 1974 스도쿠 검증 D2

for t in range(1, int(input()) + 1):
    board = [list(map(int, input().split())) for _ in range(9)]
    ans = 1
    for i in range(9):
        row = set(board[i])
        col = set([board[j][i] for j in range(9)])
        square = set()
        for j in range(3):
            for k in range(3):
                square.add(board[(i // 3) * 3 + j][(i % 3) * 3 + k])
        if len(row) != 9 or len(col) != 9 or len(square) != 9:
            ans = 0

    print(f"#{t} {ans}")
