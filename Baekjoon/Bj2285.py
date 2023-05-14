# 2258 정육점 G4

import sys


def solution():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    meats = [[0, 0, 0]]
    for i in range(N):
        meat, cost = map(int, input().split())
        meats.append([meat, cost, cost])
    meats.sort(key=lambda x: (x[1], -x[0]))
    for i in range(1, N + 1):
        if meats[i][1] == meats[i - 1][1]:
            meats[i][2] += meats[i - 1][2]
        meats[i][0] += meats[i - 1][0]
    meats.sort(key=lambda x: (x[2], -x[0]))
    for meat, cost, tcost in meats:
        if meat >= M:
            return tcost
    return -1


if __name__ == "__main__":
    print(solution())
