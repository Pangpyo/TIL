# 문제 23. 유방향 그래프 표현하기

from pprint import pprint
import sys

sys.stdin = open("input.txt")
N, M = map(int, input().split())


matrixN = [[0]*(N+1) for _ in range(N+1)]
listN = [[] for _ in range(N+1)]

for i in range(M) :
    u, v = map(int, input().split())
    matrixN[u][v] = 1
    listN[u].append(v)
pprint(matrixN)
pprint(listN)