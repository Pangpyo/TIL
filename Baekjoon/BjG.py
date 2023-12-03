# G 가희와 여행가요

import sys


def solution() :
    input = sys.stdin.readline
    sys.setrecursionlimit(10**8)
    N, Q = map(int, input().split())
    lines = [tuple(map(int, input().split())) for _ in range(Q)]
    lines.sort(key=lambda x : (x[2], x[3]))
    parents = [-1]*(N+1)
    def find(x) :
        if parents[x] < 0 :
            return x
        y = find(parents[x])
        parents[x] = y
        return y
    def union(x, y) :
        x = find(x)
        y = find(y)
        if x == y : 
            return False
        parents[min(x, y)] += parents[max(x, y)]
        parents[max(x, y)] = min(x, y)
        return True
    answer = [0, 0]
    for u, v, cost, time in lines :
        if union(u, v) :
            answer[1] += cost
            answer[0] = max(time, answer[0])
        if -parents[1] == N :
            return answer
    return [-1]

if __name__ == "__main__" :
    print(*solution())