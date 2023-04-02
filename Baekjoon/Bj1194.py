# 1194 달이 차오른다, 가자 G2

from collections import deque


def solution():
    N, M = map(int, input().split())

    miro = []
    sx = 0
    sy = 0

    for i in range(N):
        temp = list(input())
        for j in range(M):
            if temp[j] == "0":
                sx = i
                sy = j
                temp[j] = "."
        miro.append(temp)

    dic = {
        "a": 0,
        "b": 1,
        "c": 2,
        "d": 3,
        "e": 4,
        "f": 5,
        "A": 10,
        "B": 11,
        "C": 12,
        "D": 13,
        "E": 14,
        "F": 15,
    }

    visit = [[[0] * (1 << 6) for _ in range(M)] for _ in range(N)]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    que = deque([(sx, sy, 0)])
    inf = float("inf")
    ans = inf
    while que:
        x, y, keys = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            nkeys = keys
            if nx >= N or nx < 0 or ny >= M or ny < 0:
                continue
            m = miro[nx][ny]
            if m == "1":
                ans = min(visit[x][y][keys] + 1, ans)
                continue
            if visit[nx][ny][keys] or m == "#":
                continue
            if m in dic:
                a = dic[m]
                if a < 10:
                    nkeys |= 1 << a
                else:
                    if nkeys & 1 << (a - 10) == 0:
                        continue
            visit[nx][ny][nkeys] = visit[x][y][keys] + 1
            que.append((nx, ny, nkeys))

    print(ans if ans != inf else -1)


if __name__ == "__main__":
    solution()
