# 1595 북쪽나라의 도로 G4

import sys

sys.stdin = open("input.txt")
sys.setrecursionlimit(10**5)
# input = sys.stdin.readline

lines = []

while 1:
    try:
        a, b, c = map(int, input().split())
        lines.append((a, b, c))
        # lines.append(tuple(map(int, input().split())))을 사용했을땐 오류가 떴다. 대체 왜...?
    except:
        break

N = len(lines) + 1

if N == 1:
    print(0)
else:
    graph = [[] for _ in range(N + 1)]

    for i in range(1, N):
        u, v, l = lines[i - 1]
        graph[u].append((v, l))
        graph[v].append((u, l))

    def dfs(n, d):  # 트리를 탐색할 dfs.
        visit[n] = 1  # 방문처리
        go = False
        for i, l in graph[n]:
            if visit[i] == 0:  # 방문하지 않은 노드라면
                dfs(i, d + l)  # 방문해주고, 간선의 길이를 더해준다.
                go = True  # 자식노드가 있는지 판단해줄 변수
        if not go:
            leaf[n] = d  # 자식노드가 없는 노드들은 리프노드이다.

    leaf = [0] * (N + 1)  # 트리의 리프 노드를 저장할 리스트

    visit = [0] * (N + 1)  # 방문리스트
    dfs(1, 0)  # 첫 번째 노드에서 모든 노드 방문
    maxleaf = leaf.index(max(leaf))  # 특정 노드에서 가장 먼 노드 하나를 구한다.

    leaf = [0] * (N + 1)  # 가장 먼 리프 노드에서부터 다른 리프 노드까지 도달하는 거리 저장
    visit = [0] * (N + 1)  # 방문리스트
    dfs(maxleaf, 0)
    print(max(leaf))
