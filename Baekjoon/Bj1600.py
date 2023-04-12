# 1600 말이 되고픈 원숭이 G3

from collections import deque
import sys


def solution():
    input = sys.stdin.readline

    K = int(input())
    W, H = map(int, input().split())
    G = [list(map(int, input().split())) for _ in range(H)]
    inf = float("inf")
    visit = [[[inf] * (K + 1) for _ in range(W)] for _ in range(H)]
    que = deque([(0, 0, 0)])
    visit[0][0][0] = 0
    dx = [-1, 0, 1, 0, -2, -2, -1, -1, 1, 1, 2, 2]
    dy = [0, 1, 0, -1, -1, 1, -2, 2, -2, 2, -1, 1]
    while que:
        x, y, cnt = que.popleft()
        v = visit[x][y][cnt]
        for i in range(12):
            nx = x + dx[i]
            ny = y + dy[i]
            ncnt = cnt if i < 4 else cnt + 1
            if nx >= H or nx < 0 or ny >= W or ny < 0 or ncnt > K:
                continue
            if visit[nx][ny][ncnt] != inf or G[nx][ny]:
                continue
            visit[nx][ny][ncnt] = v + 1
            que.append((nx, ny, ncnt))
    ans = min(visit[-1][-1])
    return ans if ans != float("inf") else -1


if __name__ == "__main__":
    print(solution())
