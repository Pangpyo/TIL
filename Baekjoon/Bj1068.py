# 1068 트리 G5

N = int(input())

nodes = list(map(int, input().split()))
delnode = int(input())
graph = [[] for _ in range(N)]

for i in range(N):
    if nodes[i] == -1:
        start = i
    else:
        graph[nodes[i]].append(i)
ans = 0


def dfs(n):
    global ans
    point = True
    if graph[n]:
        for nn in graph[n]:
            if nn != delnode:
                dfs(nn)
                point = False

    if point:
        ans += 1


if start != delnode:
    dfs(start)

print(ans)
