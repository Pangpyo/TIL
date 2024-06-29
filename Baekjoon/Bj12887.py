# 12887 경로 게임 G5

from collections import deque


def solution():
    N = int(input())
    map_ = (input(), input())
    B = "#"
    white = N*2 - map_[0].count(B) - map_[1].count(B)
    if N == 1:
        if map_[0][0] == B or map_[1][0] == B:
            return 0
        else:
            return 1
    def bfs(x, y):
        dx = (-1, 0, 1)
        dy = (0, 1, 0)
        INF = float('inf')
        que = deque()
        que.append((x, y))
        visit = [[INF]*N for _ in range(2)]
        visit[x][y] = 1
        while que:
            x, y = que.popleft()
            v = visit[x][y]
            for i in range(3):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= 2 or ny >= N:
                    continue
                if map_[nx][ny] == B or visit[nx][ny] <= v:
                    continue
                visit[nx][ny] = v + 1
                que.append((nx, ny))
        return min(visit[0][-1], visit[1][-1])
    answer = 0
    for i in range(2):
        if map_[i][0] != B:
            answer = max(answer, white - bfs(i, 0))
    return answer

if __name__ == "__main__":
    print(solution())