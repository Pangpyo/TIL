# 16973 직사각형 탈출 G4

from collections import deque


def solution() :
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    H, W, sr, sc, fr, fc = map(int, input().split())
    sr -= 1
    sc -= 1
    fr -= 1
    fc -= 1
    que = deque()
    que.append((sr, sc))
    visit = [[0]*M for _ in range(N)]
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]


    while que :
        r, c = que.popleft()
        for i in range(4) :
            nr = r + dr[i]
            nc = c + dc[i]
            if nr + H >= N or nr < 0 or nc + W >= M or nc < 0 :
                continue
            
    return

if __name__ == "__main__" :
    print(solution())