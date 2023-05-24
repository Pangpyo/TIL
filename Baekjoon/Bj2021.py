# 2021 최소환승경로 G2

from collections import deque
import sys


def solution() :
    input = sys.stdin.readline
    N, L = map(int, input().split())
    graph = [[] for _ in range(N+1+L)]
    for s in range(N+1, N+L+1) :
        for num in map(int, input().split()) :
            if num == -1 :
                break
            graph[num].append(s)
            graph[s].append(num)
    s, e = map(int, input().split())
    que = deque([s])
    inf = sys.maxsize
    visit = [inf]*(N+1+L)
    visit[s] = -1
    if s == e :
        return 0
    while que :
        n = que.popleft()
        if n == e :
            return visit[n]
        for nn in graph[n] :
            temp = 0 if n > N else 1
            if visit[nn] <= visit[n]+temp:
                continue
            visit[nn] = visit[n]+temp
            if temp :
                que.append(nn)
            else :
                que.appendleft(nn)
    return -1

if __name__ == "__main__" :
    print(solution())