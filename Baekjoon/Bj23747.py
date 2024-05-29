# 23747 와드 G5

from collections import deque
import sys


def solution():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    map_ = tuple(input().rstrip() for _ in range(N))
    x, y = map(lambda x: int(x)-1, input().split())
    visit = [["#"]*M for _ in range(N)]
    dx = (-1, 0, 1, 0)
    dy = (0, 1, 0, -1)
    move = {'U':0, "R":1, "D":2, "L":3}
    def bfs(x, y):
        visit[x][y] = "."
        pre = map_[x][y]
        que = deque()
        que.append((x, y))
        while que:
            x, y = que.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx >= N or nx < 0 or ny >= M or ny < 0:
                    continue
                if visit[nx][ny] == "." or map_[nx][ny] != pre:
                    continue
                visit[nx][ny] = '.'
                que.append((nx, ny))
    for cmd in input().rstrip():
        if cmd == "W":
            if visit[x][y] == '#':
                bfs(x, y)
        else:
            d = move[cmd]
            x += dx[d]
            y += dy[d]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= N or nx < 0 or ny >= M or ny < 0:
            continue
        visit[nx][ny] = '.'
    visit[x][y] = '.'
    return visit

if __name__ == "__main__":
    for sol in solution():
        sys.stdout.write(''.join(sol))
        sys.stdout.write('\n')