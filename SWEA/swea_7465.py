# 7465. 창용 마을 무리의 개수 D4


import sys

sys.stdin = open("_창용마을무리의개수.txt")

T = int(input())

def dfs(a) :
    visit[a] = 1
    for person in peaple[a] : # dfs함수 생성
        if visit[person] == 0 :
            dfs(person)

for t in range(1, T+1) :
    N, M = map(int, input().split())
    visit = [0]*(N+1)
    peaple = [[] for _ in range(N+1)]
    group = 0
    for _ in range(M) :
        u, v = map(int, input().split())
        peaple[u].append(v)
        peaple[v].append(u)
    for i in range(1, N+1) :
        if visit[i] == 0 : # dfs를 실행할 때 마다 그룹의 개수를 세어준다.
            dfs(i)
            group += 1
    print('#%d'%t, group)