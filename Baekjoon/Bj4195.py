# 4195 친구 네트워크 G2


import sys


input = sys.stdin.readline


def find(x):
    if parent[x] < 0:
        return x
    else:
        y = find(parent[x])
        parent[x] = y
        return y


def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        parent[min(x, y)] += parent[max(x, y)]
        parent[max(x, y)] = min(x, y)


def check(n):
    if not n in dic:
        dic[n] = len(parent)
        parent.append(-1)


for i in range(int(input())):
    F = int(input())
    parent = []
    ans = []
    dic = {}
    for i in range(F):
        a, b = input().rsplit()
        check(a)
        check(b)
        union(dic[a], dic[b])
        ans.append(-parent[find(dic[a])])
        print(parent)
    print(*ans, sep="\n")
