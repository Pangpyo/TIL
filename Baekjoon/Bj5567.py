# 5567 결혼식 S2

from collections import deque
import sys


def solution():
    input = sys.stdin.readline
    N = int(input())
    M = int(input())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    que = deque()
    que.append(1)
    visit = [-1]*(N+1)
    visit[1] = 0
    answer = 0
    while que:
        n = que.popleft()
        v = visit[n]
        for nn in graph[n]:
            if visit[nn] != -1:
                continue
            visit[nn] = v+1
            answer += 1
            if visit[nn] < 2:
                que.append(nn)
    print(visit)
    return answer

if __name__ == "__main__":
    print(solution())