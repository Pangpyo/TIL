# 12786 INHA SUIT G4

from collections import deque
import sys


def solution():
    input = sys.stdin.readline
    N = int(input())
    T = int(input())
    MAX = 20
    trees = [[1]*(MAX+1) for _ in range(N+1)]
    for i in range(1, N+1):
        temp = map(int, input().split())
        next(temp)
        for h in temp:
            trees[i][h] = 0
    INF = sys.maxsize
    visit = [[INF]*(MAX+1) for _ in range(N+1)]
    que = deque()
    que.append((0, 1, 0))
    visit[0][1] = 0
    while que:
        n, h, d = que.popleft()
        if visit[n][h] < d:
            continue
        can_move = (h-1, h, h+1, min(MAX, h*2))
        for i in range(1, MAX+1):
            if trees[n+1][i]:
                continue
            use_t = int(i not in can_move)
            nd = d + use_t
            if visit[n+1][i] <= nd:
                continue
            visit[n+1][i] = nd
            if n+1 == N:
                continue
            if use_t:
                que.append((n+1, i, nd))
            else:
                que.appendleft((n+1, i, nd))
    answer = min(visit[-1])
    return answer if answer <= T else -1

if __name__ == "__main__":
    print(solution())