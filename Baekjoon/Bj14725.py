# 14725 개미굴 G3


import sys


def solution() :
    input = sys.stdin.readline
    N = int(input())
    graph = {}
    for _ in range(N) :
        temp = list(input().split())
        k = temp[0]
        pre = graph
        for c in temp[1::] :
            if c not in pre :
                pre[c] = {}
            pre = pre[c]
    def dfs(pre : dict, deep) :
        bar = "--" * deep
        for k, v in sorted(pre.items()) :
            print(bar+k)
            dfs(v, deep+1)
    dfs(graph, 0)
    return 
if __name__ == "__main__" :
    solution()