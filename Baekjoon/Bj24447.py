# 24447 알고리즘 수업 - 너비 우선 탐색 4

from collections import deque
import sys


def solution():
    input = sys.stdin.readline
    N, M, R = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    for g in graph:
        g.sort()
    visit = [-1]*(N+1)
    que = deque()
    que.append(R)
    visit[R] = 0
    order = [0]*(N+1)
    order[R] = 1
    o = 1
    while que:
        x = que.popleft()
        v = visit[x]
        for nx in graph[x]:
            if visit[nx] != -1:
                continue
            visit[nx] = v + 1
            o += 1
            order[nx] = o
            que.append(nx)
    answer = 0
    for i in range(1, N+1):
        if visit[i] != -1:
            answer += visit[i]*order[i]
    return answer

if __name__ == "__main__":
    print(solution())