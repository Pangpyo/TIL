# 2606 바이러스 S3

import sys

sys.stdin = open("input.txt")

N = int(input())

M = int(input())
network = [[] for _ in range(N+1)]
for i in range(M) :
    u, v = map(int, input().split())
    network[u].append(v)
    network[v].append(u)
visit = [0] * (N+1) # 방문한 컴퓨터를 표시
def dfs(u) : # 
    visit[u] = 1 # u번째 컴퓨터에 방문
    for i in network[u] : # u번째 컴퓨터와 연결된 컴퓨터들을 모두 방문
        if visit[i] == 0 : # 방문 할 컴퓨터가 방문하지 않은 컴퓨터일시
            dfs(i) # dfs함수를 통해 해당 컴퓨터와 연결된 컴퓨터들 다시 방문
dfs(1)

print(sum(visit)-1)
