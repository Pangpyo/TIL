# 29160 나의 FIFA 팀 가치는?

from heapq import heappop, heappush
import sys


def solution() :
    input = sys.stdin.readline
    N, K = map(int, input().split())
    players = [[] for _ in range(12)]
    team = [0]*(12)
    for i in range(N) :
        p, w = map(int, input().split())
        heappush(players[p], -w)
    for k in range(K+1) :
        for i in range(1, 12) :
            if players[i] :
                team[i] = heappop(players[i])
        if k == K :
            break
        for i in range(1, 12) :
            if team[i] <= -1:
                team[i] += 1
                heappush(players[i], team[i])
    return -sum(team)

if __name__ == "__main__" :
    print(solution())