# 23083 꿀벌 승연이 G5

import sys


def solution() :
    input = sys.stdin.readline
    N, M = map(int, input().split())
    H = [[0]*M for _ in range(N)]
    K = int(input())
    for _ in range(K) :
        x, y = map(int, input().split())
        H[x-1][y-1] = 1
    D = [[0]*M for _ in range(N)]
    D[0][0] = 1
    dx = [-1, 1, 0, 1]
    dy = [1, 0, 1, 1]
    div = 10**9 + 7
    for y in range(M) :
        for x in range(N) :
            if H[x][y] :
                continue
            for i in range(3) :
                j = 1 if y % 2 else 0
                nx = x + dx[i+j]
                ny = y + dy[i+j]
                if nx < 0 or nx >= N or ny >= M :
                    continue
                D[nx][ny] = (D[nx][ny] + D[x][y])%div
    return D[-1][-1]

if __name__ == "__main__" :
    print(solution())