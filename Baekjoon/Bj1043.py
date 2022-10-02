# 1043 거짓말 G4

import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline


def bfs(u):
    visit[u] = 1
    for v in graph[u]:
        if not visit[v]:
            bfs(v)


N, M = map(int, input().split())

know = list(map(int, input().split()))
if know[0] == 0:
    print(M)
else:
    graph = [[] for _ in range(N + 1)]
    partys = []
    for i in range(M):
        party = list(map(int, input().split()))
        partys.append(party)
        for u in range(1, party[0] + 1):
            for v in range(1, party[0] + 1):
                if u == v:
                    continue
                graph[party[u]].append(party[v])
    visit = [0] * (N + 1)
    for i in range(1, know[0] + 1):
        bfs(know[i])
    ans = 0
    for party in partys:
        canlie = True
        for i in range(1, party[0] + 1):
            if visit[party[i]] == 1:
                canlie = False
                break
        if canlie:
            ans += 1
    print(ans)
