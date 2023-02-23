def solution(boards):
    global flag
    answer = []
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    def dfs(x, y, cnt):
        global flag
        if flag:
            return
        if cnt == g:
            flag = True
            return
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= N or nx < 0 or ny >= M or ny < 0:
                continue
            if board[nx][ny] != "1":
                continue
            board[nx][ny] = "2"
            dfs(nx, ny, cnt + 1)
            board[nx][ny] = "1"

    for t in range(len(boards)):
        N = len(boards[t])
        M = len(boards[t][0])
        board = []
        for i in range(N):
            board.append(list(boards[t][i]))
        g = 0
        sx = 0
        sy = 0
        for i in range(N):
            for j in range(M):
                if board[i][j] == "1":
                    g += 1
                elif board[i][j] == "2":
                    sx = i
                    sy = j
        flag = False
        dfs(sx, sy, 0)
        if flag:
            answer.append(1)
        else:
            answer.append(0)
    return answer

