# 16469 소년점프 G4

from collections import deque
import sys


def solution() :
    input = sys.stdin.readline
    N, M = map(int, input().split())
    miro = [list(map(int, list(input().rstrip()))) for _ in range(N)]
    times = [[[-1, -1, -1] for _ in range(M)] for _ in range(N)]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    for i in range(3) :
        x, y = map(int, input().split())
        que = deque()
        times[x-1][y-1][i] = 0
        que.append((x-1, y-1))
        while que :
            x, y = que.popleft()
            for d in range(4) :
                nx = x + dx[d]
                ny = y + dy[d]
                if nx >= N or nx < 0 or ny >= M or ny < 0 :
                    continue
                if times[nx][ny][i] != -1 or miro[nx][ny]:
                    continue
                times[nx][ny][i] = times[x][y][i] + 1
                que.append((nx, ny))
    ans = []
    for i in range(N) :
        for j in range(M) :
            flag = True
            temp = 0
            for k in range(3) :
                if times[i][j][k] == -1 :
                    flag = False
                    break
                else :
                    temp = max(temp, times[i][j][k])
            if flag :
                ans.append(temp)
    ans.sort()
    if not ans :
        print(-1)
    else :
        cnt = 0
        t = ans[0]
        for a in ans :
            cnt += 1 if a == t else 0
        print(t, cnt, sep="\n")

if __name__ == "__main__" :
    solution()