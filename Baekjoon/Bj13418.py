# 13418 학교 탐방하기 G3

import sys


def solution() :
    input = sys.stdin.readline
    N, M = map(int, input().split())
    lines = [tuple(map(int, input().split())) for _ in range(M+1)]
    
    def find(x) :
        if parent[x] < 0 :
            return x
        y = find(parent[x])
        parent[x] = y
        return y
    def union(x, y) :
        x = find(x)
        y = find(y)
        if x == y :
            return False
        parent[min(x, y)] += parent[max(x, y)]
        parent[max(x, y)] = min(x, y)
        return True
    
    def kruskal() :
        dist = 0
        for u, v, d in lines :
            if union(u, v) :
                dist += 0 if d else 1
            if parent[0] == -(N+1) :
                break
        return dist
    
    parent = [-1]*(N+1)
    lines.sort(key = lambda x : -x[2])
    mind = kruskal()
    parent = [-1]*(N+1)
    lines.sort(key = lambda x : x[2])
    maxd = kruskal()
    return maxd*maxd-mind*mind

if __name__ == "__main__" :
    print(solution())