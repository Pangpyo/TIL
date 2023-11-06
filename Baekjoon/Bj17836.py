# 17836 공주님을 구해라! G5

from collections import deque
import sys


def solution() :
    input = sys.stdin.readline
    N, M, T = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(N)]
    inf = sys.maxsize
    D = [[[inf, inf] for _ in range(M)] for _ in range(N)]
    que = deque()
    que.append((0, 0, 0))
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    D[0][0][0] = 0
    while que :
        x, y, g = que.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            ng = g
            if nx >= N or nx < 0 or ny >= M or ny < 0 :
                continue
            if P[nx][ny] == 2 :
                ng = 1
            elif P[nx][ny] == 1 :
                if not g :
                    continue
            if D[nx][ny][ng] != inf :
                continue
            D[nx][ny][ng] = D[x][y][g] + 1
            que.append((nx, ny, ng))
    answer = min(D[-1][-1])
    if answer > T :
        return "Fail"
    return answer

if __name__ == "__main__" :
    print(solution())