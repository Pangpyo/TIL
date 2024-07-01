# 26146 즉흥 여행 (Easy) P5

import sys


def solution():
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u-1].append(v-1)
    visit = [-1]*V
    stack = []
    on_stack = [0]*V
    idx = 0
    sccs = []
    def dfs(x):
        nonlocal idx
        idx += 1
        stack.append(x)
        visit[x] = idx
        on_stack[x] = 1
        parent = visit[x]
        for nx in graph[x]:
            if visit[nx] == -1:
                parent = min(parent, dfs(nx))
            elif on_stack[nx]:
                parent = min(parent, visit[nx])
        if parent == visit[x]:
            scc = []
            while stack:
                node = stack.pop()
                on_stack[node] = 0
                scc.append(node+1)
                if x == node:
                    break
            sccs.append(scc)
        return parent
    for i in range(V):
        if visit[i] == -1:
            dfs(i)
    return "Yes" if len(sccs) == 1 else "No"

if __name__ == "__main__":
    print(solution())