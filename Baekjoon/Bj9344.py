# 9344 도로 G3

import sys


def solution():
    input = sys.stdin.readline
    T = int(input())
    answers = ["NO"]*T
    YES = "YES"
    def find(x):
        if parents[x] == x:
            return x
        y = find(parents[x])
        parents[x] = y
        return y
    
    def union(x, y):
        x = find(x)
        y = find(y)
        if x == y:
            return False
        parents[max(x, y)] = min(x, y)
        return True

    for t in range(T):
        N, M, p, q = map(int, input().split())
        p, q = min(p, q), max(p, q)
        lines = [tuple(map(int, input().split())) for _ in range(M)]
        lines.sort(key=lambda x: x[2])
        parents = list(range(N+1))
        for x, y, d in lines:
            if union(x, y):
                if min(x, y) == p and max(x, y) == q:
                    answers[t] = YES
                
    return answers

if __name__ == "__main__":
    print(*solution(), sep='\n')