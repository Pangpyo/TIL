# 16973 직사각형 탈출 G4

from collections import deque


def solution() :
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    H, W, sr, sc, fr, fc = map(int, input().split())
    H -= 1
    W -= 1
    sr -= 1
    sc -= 1
    fr -= 1
    fc -= 1
    que = deque()
    que.append((sr, sc))
    visit = [[0]*M for _ in range(N)]
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    visit[sr][sc] = 1
    while que :
        r, c = que.popleft()
        d = visit[r][c]
        for i in range(4) :
            nr = r + dr[i]
            nc = c + dc[i]
            if nr + H >= N or nr < 0 or nc + W >= M or nc < 0 :
                continue
            flag = False
            if visit[nr][nc] :
                continue
            if dr[i] :
                temp = 0 if dr[i] == -1 else H
                for j in range(W+1) :
                    if board[nr+temp][nc+j] :
                        flag = True
                        break
            else :
                temp = 0 if dc[i] == -1 else W
                for j in range(H+1) :
                    if board[nr+j][nc+temp] :
                        flag = True
                        break 
            if flag :
                continue
            if nr == fr and nc == fc :
                return d
            visit[nr][nc] = d+1
            que.append((nr, nc))
        
    return -1

if __name__ == "__main__" :
    print(solution())