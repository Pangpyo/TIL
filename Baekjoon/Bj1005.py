# 1005 ACM Craft G3

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def answer(n):
    if dp[n] == inf:
        temp = 0
        for nn in parent[n]:
            temp = max(temp, answer(nn))
        dp[n] = temp + D[n]
    return dp[n]


ans = []

for _ in range(int(input())):
    N, K = map(int, input().split())
    D = list(map(int, input().split()))
    parent = [[] for _ in range(N)]
    for i in range(K):
        u, v = map(int, input().split())
        parent[v - 1].append(u - 1)

    W = int(input()) - 1
    inf = sys.maxsize
    dp = [inf] * N

    ans.append(answer(W))

print(*ans, sep="\n")
