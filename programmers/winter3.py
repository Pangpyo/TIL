from collections import deque


def solution(worldmap):
    N = len(worldmap)
    M = len(worldmap[0])
    visit = [[0] * M for _ in range(N)]
    que = deque([(0, 0, 0, 0)])
    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    dy = [1, 1, 0, -1, -1, -1, 0, 1]
    answer = 0
    while que:
        x, y, d, t = que.popleft()
        print(x, y, d, t)
        visit[x][y] = 1
        if x == N - 1 and y == M - 1:
            answer = t
            break
        directions = []
        if d % 2 == 1:
            directions = [(d + 7) % 8, (d + 1) % 8]
        else:
            directions = [(d + 7) % 8, d % 8, (d + 1) % 8]
        for a in directions:
            nx = x + dx[a]
            ny = y + dy[a]
            if nx >= N or nx < 0 or ny >= M or ny < 0:
                continue
            if worldmap[nx][ny] == "X":
                continue
            if a % 2 == 1:
                prex = nx + dx[(a + 7) % 8]
                prey = ny + dy[(a + 7) % 8]
                aftx = nx + dx[(a + 1) % 8]
                afty = ny + dy[(a + 1) % 8]
                print("좌표 :", prex, prey, aftx, afty)
                prego = True
                aftgo = True
                if prex >= N or prex < 0 or prey >= M or prey < 0:
                    pass
                else:
                    if worldmap[prex][prey] == "X":
                        prego = False
                if aftx >= N or aftx < 0 or afty >= M or afty < 0:
                    pass
                else:
                    if worldmap[aftx][afty] == "X":
                        atfgo = False
                if not prego and not aftgo:
                    continue

            que.append((nx, ny, a, t + 1))

    return answer


worldmap = ["..XXX....", "..XXX....", "...XX....", "X........", "XX....X.."]

print(solution(worldmap))
