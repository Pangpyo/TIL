# 1900 레슬러 S1

import sys


def solution():
    input = sys.stdin.readline
    N = int(input())
    players = [tuple(map(int, input().split())) for _ in range(N)]
    wins = [0]*N
    for i, player in enumerate(players):
        p, r = player
        for j in range(i+1, N):
            np, nr = players[j]
            if p + r * np > np + nr * p:
                wins[i] += 1
                wins[j] -= 1
            else:
                wins[j] += 1
                wins[i] -= 1
    lines = list(range(1, N+1))
    lines.sort(key=lambda x: -wins[x-1])
    return lines

if __name__ == "__main__":
    print(*solution(), sep='\n')