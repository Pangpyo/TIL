# 16928 뱀과 사다리 게임 G5

from collections import deque
import sys

input = sys.stdin.readline
N, M = map(int, input().split())


def bfs():
    visit = [0] * 101
    que = deque([(1)])
    move = [0] * 101
    for _ in range(N):
        u, v = map(int, input().split())
        move[u] = v
    for _ in range(M):
        u, v = map(int, input().split())
        move[u] = v
    while que:
        n = que.popleft()
        for i in range(1, 7):
            nn = n + i
            if nn > 100:
                continue
            if not visit[nn]:
                visit[nn] = visit[n] + 1
                if move[nn]:
                    if visit[move[nn]]:
                        continue
                    visit[move[nn]] = visit[nn]
                    que.append(move[nn])
                    if move[nn] == 100:
                        return visit[-1]
                else:
                    que.append(nn)
                    if nn == 100:
                        return visit[-1]


print(bfs())
