# 15558 점프 게임 G5

from collections import deque


def solution() :
    N, k = map(int, input().split())
    P = [input(), input()]
    que = deque()
    que.append((0, 0, 0))
    visit = [[0]*N for _ in range(2)]
    visit[0][0] = 1
    while que :
        x, y, t = que.popleft()
        for nx, ny in ((x, y+1), (x, y-1), ((x+1)%2, y+k)) :
            if ny >= N :
                return 1
            if ny < t+1 or visit[nx][ny] or P[nx][ny] == '0' :
                continue
            visit[nx][ny] = 1
            que.append((nx, ny, t+1))

    return 0

if __name__ == "__main__" :
    print(solution())