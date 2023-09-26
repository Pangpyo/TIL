# 22944 죽음의 비 G3

from collections import deque
import sys


def solution() :
    input = sys.stdin.readline
    N, H, D = map(int, input().split())
    S = []
    sx, sy = 0, 0
    ex, ey = 0, 0
    K = 1
    for i in range(N) :
        temp = input().rstrip()
        tempS = [0]*N
        for j in range(N) :
            if temp[j] == "S" :
                sx, sy = i, j
            elif temp[j] == "U" :
                tempS[j] = K
                K += 1
            elif temp[j] == "E" :
                ex, ey = i, j
                tempS[j] = -1
        S.append(tempS)

    que = deque()
    que.append((sx, sy, H, 0, 0, 0))
    visit = [[[-1]*(K) for _ in range(N)] for _ in range(N)]
    dx = (-1, 0, 1, 0)
    dy = (0, 1, 0, -1)
    visit[sx][sy][0] = 0
    while que :
        x, y, h, d, k, v = que.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            nh, nd, nk, nv = h, d, k, v
            if nx >= N or nx < 0 or ny >= N or ny < 0 :
                continue
            if S[nx][ny] > 0 :
                if v & (1<<S[nx][ny]) :
                    continue
            if S[nx][ny] > 0 :
                nk += 1
                nd = D
                nv |= (1<<S[nx][ny])
            if S[nx][ny] != -1 :
                if nd :
                    nd -= 1
                else :
                    nh -= 1
            if nh == 0 or visit[nx][ny][nk] >= 0 :
                continue
            visit[nx][ny][nk] = visit[x][y][k] + 1
            if S[nx][ny] == 'E' :
                continue
            que.append((nx, ny, nh, nd, nk, nv))
    answer = sys.maxsize
    for i in range(K) :
        if visit[ex][ey][i] > 0 :
            answer = min(answer, visit[ex][ey][i])
    return answer if answer != sys.maxsize else -1

if __name__ == "__main__" :
    print(solution())