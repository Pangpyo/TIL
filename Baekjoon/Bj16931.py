# 16931 겉넓이 구하기 S2

import sys


def solution():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    paper = tuple(tuple(map(int, input().split())) for _ in range(N))
    answer = N*M*2
    
    for i in range(N):
        l, r = 0, 0
        for j in range(M):
            answer += max(0, paper[i][j] - l) + max(0, paper[i][-1-j] - r)
            l = paper[i][j]
            r = paper[i][-1-j]
    for j in range(M):
        u, d = 0, 0
        for i in range(N):
            answer += max(0, paper[i][j] - u) + max(0, paper[-1-i][j] - d)
            u = paper[i][j]
            d = paper[-1-i][j]
    return answer


if __name__ == '__main__':
    print(solution())