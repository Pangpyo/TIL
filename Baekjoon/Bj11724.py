# 11724 연결 요소의 개수 S2

import sys


sys.stdin = open('input.txt')

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]

for i in range(M) :
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visit = [0] * (N+1) # 방문한 정점을 표시
def dfs(u) : 
    visit[u] = 1 # u번째 정점에 방문
    for i in graph[u] : # u번째 정점과 연결된 정점들을 모두 방문
        if visit[i] == 0 : # 방문 할 정점이 방문하지 않은 정점일시
            dfs(i)
connected = 0
for i in range(1, N+1) :
    if visit[i] == 0 :   
        dfs(i)
        connected += 1 
    # 각 정점에서 dfs를 실행하고 dfs함수가 실행된 횟수가 연결요소의 개수가 됨

print(connected)
