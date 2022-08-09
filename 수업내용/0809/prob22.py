# 문제 22. 무방향 그래프 표현하기

from pprint import pprint
import sys

sys.stdin = open("input.txt")
N, M = map(int, input().split())


matrixN = [[0]*(N+1) for _ in range(N+1)]
listN = [[] for _ in range(N+1)]
for i in range(M) :
    u, v = map(int, input().split())
    matrixN[u][v] = 1 # 양 방향으로 이어져있으므로 
    matrixN[v][u] = 1 # v, u의 경우도 저장
    listN[u].append(v) # 마찬가지로 양 방향이므로 
    listN[v].append(u) # v, u의 경우도 생각한다.
pprint(matrixN)
pprint(listN)