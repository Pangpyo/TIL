# 14267 회사문화 1 G4


import sys

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n, m = map(int, input().split())

nodes = list(map(int, input().split()))
graph = [[] for _ in range(n)]

for i in range(n):
    if nodes[i] == -1:
        start = i
    else:
        graph[nodes[i] - 1].append(i)

score = [0] * n


def dfs(n):
    if graph[n]:
        for nn in graph[n]:
            score[nn] += score[n]
            dfs(nn)


for i in range(m):
    a, b = map(int, input().split())
    score[a - 1] += b

dfs(0)
print(*score)
