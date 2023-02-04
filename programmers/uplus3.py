from pprint import pprint


def solution(macaron):

    board = [[0] * 6 for _ in range(6)]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    def check(x, y):
        color = board[x][y]
        stack = [(x, y)]
        blocks = [(x, y)]
        while stack:
            x, y = stack.pop()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx >= 6 or nx < 0 or ny >= 6 or ny < 0:
                    continue
                if visit[nx][ny]:
                    continue
                if board[nx][ny] == color:
                    visit[nx][ny] = 1
                    stack.append((nx, ny))
                    blocks.append((nx, ny))
        print(color, blocks)
        if len(blocks) >= 3:
            for x, y in blocks:
                board[x][y] = 0
            drop()
            return True
        else:
            return False

    def drop():
        for j in range(6):
            ntemp = [0] * 6
            idx = 0
            for i in reversed(range(6)):
                if board[i][j]:
                    ntemp[idx] = board[i][j]
                    idx += 1
            for i in reversed(range(6)):
                board[i][j] = ntemp[-i - 1]
        global visit
        visit = [[0] * 6 for _ in range(6)]
        pprint(board)
        for i in range(6):
            for j in range(6):
                if board[i][j]:
                    visit[i][j] = 1
                    check(i, j)

    for y, color in macaron:
        board[0][y - 1] = color
        drop()
        pprint(board)
    answer = []
    for i in range(6):
        answer.append("".join(map(str, board[i])))

    return answer


macaron = [
    [1, 1],
    [2, 1],
    [1, 2],
    [3, 3],
    [6, 4],
    [3, 1],
    [3, 3],
    [3, 3],
    [3, 4],
    [2, 1],
]

print(solution(macaron))
