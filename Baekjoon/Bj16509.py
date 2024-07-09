# 16509 장군 G5

from collections import deque


def solution():
    R = 10
    C = 9
    visit = [[-1]*C for _ in range(R)]
    sr, sc = map(int, input().split())
    er, ec = map(int, input().split())
    visit[sr][sc] = 0
    que = deque([(sr, sc)])
    dr = ((-1, -2, -3), (-1, -2, -3), (0, -1, -2), (0, 1, 2), (1, 2, 3), (1, 2, 3), (0, 1, 2), (0, -1, -2))
    dc = ((0, -1, -2), (0, 1, 2), (1, 2, 3), (1, 2, 3), (0, 1, 2), (0, -1, -2), (-1, -2, -3), (-1, -2, -3))
    def can_move(r, c, d):
        for i in range(3):
            nr = r + dr[d][i]
            nc = c + dc[d][i]
            if nr >= R or nr < 0 or nc >= C or nc < 0:
                return False
            if i < 2 and (nr, nc) == (er, ec):
                return False
        return True
    while que:
        r, c = que.popleft()
        v = visit[r][c]
        for i in range(8):
            if not can_move(r, c, i):
                continue
            nr, nc = r + dr[i][2], c + dc[i][2]
            if visit[nr][nc] != -1:
                continue
            visit[nr][nc] = v + 1
            if (nr, nc) == (er, ec):
                return visit[nr][nc]
            que.append((nr, nc))
    return -1

if __name__ == "__main__":
    print(solution())