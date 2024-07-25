# 14400 편의점 2 S2

import sys


def solution():
    input = sys.stdin.readline
    N = int(input())
    X = []
    Y = []
    for _ in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    answer = 0
    X.sort()
    Y.sort()
    midx = X[(N-1)//2]
    midy = Y[(N-1)//2]
    for x, y in zip(X, Y):
        answer += abs(x-midx) + abs(y-midy)
    
    return answer
if __name__ == "__main__":
    print(solution())