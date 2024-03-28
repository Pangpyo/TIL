# 21738 얼음 깨기 G5

from collections import deque
import sys


def solution() :
    input = sys.stdin.readline
    N, S, P = map(int, input().split())
    que = deque()
    visit = [-1]*(N+1)
    que.append(P)
    visit[P] = 0
    graph = [[] for _ in range(N+1)]
    for _ in range(N-1) :
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    while que :
        n = que.popleft()
        for nn in graph[n] :
            if visit[nn] != -1:
                continue
            que.append(nn)
            visit[nn] = visit[n] + 1
    min_ice = sum(sorted(visit[1:S+1])[0:2])
    answer = N - 1 - min_ice
    return answer

if __name__ == "__main__" :
    print(solution())