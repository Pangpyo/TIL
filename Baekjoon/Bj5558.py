# 5558 チーズ (Cheese) G5

from collections import deque
import sys


def solution():
    input = sys.stdin.readline
    N, M, K = map(int, input().split())
    map_ = []
    x, y = 0, 0
    for i in range(N):
        temp = list(input().rstrip())
        for j in range(M):
            if temp[j] == 'S':
                temp[j] = 0
                x, y = i, j
            elif temp[j].isdigit():
                temp[j] = int(temp[j])
        map_.append(temp)
    dx = (-1, 0, 1, 0)
    dy = (0, 1, 0, -1)
    def bfs(x, y):
        if map_[x][y] == K:
            return 0
        que = deque()
        que.append((x, y))
        visit = [[-1]*M for _ in range(N)]
        visit[x][y] = 0
        s = map_[x][y]
        while que:
            x, y = que.popleft()
            v = visit[x][y]
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx >= N or nx < 0 or ny >= M or ny < 0:
                    continue
                if map_[nx][ny] == 'X' or visit[nx][ny] != -1:
                    continue
                visit[nx][ny] = v + 1
                if map_[nx][ny] == s + 1:
                    return visit[nx][ny] + bfs(nx, ny)
                que.append((nx, ny))
        return 0
    return bfs(x, y)

if __name__ == "__main__":
    print(solution())