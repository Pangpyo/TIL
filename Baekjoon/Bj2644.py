# 2644 촌수 계산 S2

import sys


sys.stdin = open('input.txt')

N = int(input())

A, B = map(int,input().split())

graph = [[] for _ in range(N+1)]

M = int(input())

for i in range(M) :
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

chon = [-1]*(N+1)
chon[A] = 0 # 첫 번째 사람의 촌수를 0으로 설정
def dfs(a) :
    for i in graph[a] : # u번째 정점과 연결된 정점들을 모두 방문
        if chon[i] == -1 : # 방문하지 않은 정점 방문
            chon[i] = chon[a] +1 # 방문한 사람의 촌수는 직전의 촌수에서 +1
            dfs(i)
            
dfs(A)

print(chon[B]) # 두번째 사람의 촌수 출력