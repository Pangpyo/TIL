# 16964 DFS 스페셜 저지 G3

from collections import deque
import sys


input = sys.stdin.readline

N = int(input())

graph = [set() for _ in range(N + 1)]

for i in range(N - 1):
    u, v = map(int, input().split())
    graph[u].add(v)
    graph[v].add(u)


user = deque(map(int, input().split()))


def dfs(n):
    while graph[n]:
        nn = 0
        if user and graph[n]:
            nn = user.popleft()
        else:
            return
        if nn in graph[n]:
            graph[n].remove(nn)
            graph[nn].remove(n)
            dfs(nn)
        else:
            print(0)
            exit()


if user[0] == 1:
    dfs(user.popleft())
    print(1)
else:
    print(0)
