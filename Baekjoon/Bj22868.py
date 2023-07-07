# 22868 산책 (small) G3

from collections import deque
import sys


def solution() :
    input = sys.stdin.readline
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]

    for _ in range(M) :
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    s, e = map(int, input().split())

    for i in range(1, N+1) :
        graph[i].sort()

    visit = [0]*(N+1)
    route = [0]*(N+1)
    que = deque()
    que.append(s)
    visit[s] = 1
    flag = False
    while que :
        n = que.popleft()
        d = visit[n]
        for nn in graph[n] :
            if visit[nn] :
                continue
            route[nn] = n
            if nn == e :
                flag = True
                break
            que.append(nn)
            visit[nn] = d+1
        if flag :
            break
    ans = d
    used = set()
    pre = e

    while True :
        pre = route[pre]
        if pre == s :
            break
        used.add(pre)
    visit = [0]*(N+1)
    que = deque()
    que.append(e)
    visit[e] = 1
    flag = False
    while que :
        n = que.popleft()
        d = visit[n]
        for nn in graph[n] :
            if visit[nn] or nn in used :
                continue
            if nn == s :
                flag = True
                break
            que.append(nn)
            visit[nn] = d+1
        if flag :
            break
    ans += d
    return ans

if __name__ == "__main__" :
    print(solution())