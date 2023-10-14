# 1584 게임 G5

from collections import deque
import sys


def solution() :
    input = sys.stdin.readline
    ground = [[0]*501 for _ in range(501)]

    for _ in range(int(input())) :
        sx, sy, ex, ey = map(int, input().split())
        sx, ex = min(sx, ex), max(sx, ex)
        sy, ey = min(sy, ey), max(sy, ey)
        for x in range(sx, ex+1) :
            for y in range(sy, ey+1) :
                ground[x][y] = 1
    for _ in range(int(input())) :
        sx, sy, ex, ey = map(int, input().split())
        sx, ex = min(sx, ex), max(sx, ex)
        sy, ey = min(sy, ey), max(sy, ey)
        for x in range(sx, ex+1) :
            for y in range(sy, ey+1) :
                ground[x][y] = 2
    inf = sys.maxsize
    D = [[inf]*501 for _ in range(501)]
    D[0][0] = 0
    que = deque()
    que.append((0, 0))
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    while que :
        x, y = que.popleft()
        d = D[x][y]
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 501 or nx < 0 or ny >= 501 or ny < 0 :
                continue
            if ground[nx][ny] == 2 :
                continue
            nd = d + ground[nx][ny]
            if nd >= D[nx][ny] :
                continue
            D[nx][ny] = nd
            if ground[nx][ny] :
                que.append((nx, ny))
            else :
                que.appendleft((nx, ny))
            
    return D[-1][-1] if D[-1][-1] != inf else -1

if __name__ == "__main__" :
    print(solution())