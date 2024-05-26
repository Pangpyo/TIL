# 2666 벽장문의 이동 G5

import sys


def solution():
    input = sys.stdin.readline
    N = int(input())
    a, b = map(int, input().split())
    INF = sys.maxsize
    K = int(input())
    orders = tuple(int(input()) for _ in range(K))
    visit = [[[INF]*(N+1) for _ in range(N+1)] for _ in range(K+1)]
    visit[0][a][b] = 0
    for n in range(1, K+1):
        o = orders[n-1]
        for i in range(1, N+1):
            for j in range(1, N+1):
                if i == j:
                    continue
                visit[n][o][j] = min(visit[n][o][j], visit[n-1][i][j] + abs(o-i))
                visit[n][i][o] = min(visit[n][i][o], visit[n-1][i][j] + abs(o-j))
    answer = min(map(min, visit[-1]))
    return answer

if __name__ == "__main__":
    print(solution())