# 1135 뉴스전하기 G2

N = int(input())

tree = list(map(int, input().split()))

graph = [[] for _ in range(N)]

for i in range(1, N):
    graph[tree[i]].append(i)

D = [-1] * N


def time(n):
    D[n] = len(graph[n])
    temp = []
    for nn in graph[n]:
        temp.append(time(nn))
    temp.sort(reverse=True)
    for i, t in enumerate(temp):
        D[n] = max(t + i + 1, D[n])
    return D[n]


print(time(0))
