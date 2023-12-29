# 23352 방탈출 G5

from collections import deque


def solution() :
    N, M = map(int, input().split())
    miro = tuple(tuple(map(int, input().split())) for _ in range(N))
    dx = (-1, 0, 1, 0)
    dy = (0, 1, 0, -1)
    def bfs(x, y) :
        que = deque()
        que.append((x, y))
        visit = [[-1]*M for _ in range(N)]
        value = 0
        dist = 0
        visit[x][y] = 0
        while que :
            x, y = que.popleft()
            for i in range(4) :
                nx = x + dx[i]
                ny = y + dy[i]
                if nx >= N or nx < 0 or ny >= M or ny < 0 :
                    continue
                if visit[nx][ny] != -1 or not miro[nx][ny] :
                    continue
                visit[nx][ny] = visit[x][y] + 1
                que.append((nx, ny))
        for i in range(N) :
            for j in range(M) :
                if visit[i][j] > dist :
                    value = miro[i][j]
                    dist = visit[i][j]
                elif visit[i][j] == dist :
                    value = max(value, miro[i][j])
        return dist, value 
    max_dist = 0
    answer = 0
    for i in range(N) :
        for j in range(M) :
            if miro[i][j] :
                dist, value = bfs(i, j)
                if not value :
                    continue
                if dist > max_dist :
                    max_dist = dist
                    answer = value+miro[i][j]
                elif dist == max_dist :
                    answer = max(answer, value+miro[i][j])
    return answer

if __name__ == "__main__" :
    print(solution())