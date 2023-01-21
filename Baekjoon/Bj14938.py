# 14938 서강그라운드 G4

import sys

input = sys.stdin.readline

N, M, R = map(int, input().split())

items = list(map(int, input().split()))

graph = [[10**5] * (N) for _ in range(N)]  # 모든 노드를 최대값으로 초기화

for i in range(R):
    u, v, d = map(int, input().split())
    graph[u - 1][v - 1] = d  # 양방향 그래프
    graph[v - 1][u - 1] = d

for i in range(N):  # 자기 자신과의 거리를 나타내는 부분은 0으로 초기화
    graph[i][i] = 0


for k in range(N):  # 플로이드 워셜. k노드를 경유했을 때 i노드와 j노드 사이의 최소거리를 찾는다.
    for i in range(N):
        for j in range(N):
            graph[i][j] = min(
                graph[i][j], graph[i][k] + graph[k][j]
            )  # 기존의 거리와 k를 경유한 경우의 거리중 최소값을 찾는다


ans = 0
for i in range(N):
    temp = 0
    for j in range(N):
        if graph[i][j] <= M:  # 범위 안에 있는 경우 아이템의 개수를 더해줌
            temp += items[j]
    ans = max(temp, ans)  # 얻을 수 있는 아이템의 최대값 저장

print(ans)
