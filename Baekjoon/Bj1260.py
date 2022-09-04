# 1260 DFS와 BFS S2


from collections import deque


N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)] #

for _ in range(1, M+1) : # 그래프 생성
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
for g in graph : # 문제의 조건에서 방문 할 수 있는 정점이 여러개인 경우 정점 번호가 작은 것을 먼저 방문하므로, sort해줌
    g.sort()

print(graph)


visitdfs = [0]*(N+1)
def dfs(x) : # 기본적인 dfs함수 생성. 한 점을 방문하면 이어진 점들을 계속 방문한다.
    print(x, end=' ')
    visitdfs[x] = 1
    for i in graph[x] :
        if visitdfs[i] == 0 :
            dfs(i)

visitbfs = [0]*(N+1)
def bfs(x) : # 기본적인 bfs함수 생성. 한 점을 방문하면 그 점에서 방문할 수 있는 모든 점들을 탐색 한 후, 다음 점들에서 이어진 점들을 방문한다.
    print(x, end=' ')
    visitbfs[x] = 1
    que = deque()
    que.append(graph[x])
    while que :
        temp = que.popleft()
        for i in temp :
            if visitbfs[i] == 0 :
                print(i, end = ' ')
                visitbfs[i] = 1
                que.append(graph[i])

dfs(V)
print()
bfs(V)