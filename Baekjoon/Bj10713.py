# 10713 기차 여행 G5

from itertools import accumulate
import sys


def solution():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    P = list(map(int, input().split()))
    visit = [0]*(N+2)
    costs = tuple(tuple(map(int, input().split())) for _ in range(N-1))
    for i in range(1, M) :
        p = P[i-1]
        n = P[i]
        s, e = min(p, n), max(p, n)
        visit[s] += 1
        visit[e] -= 1
    prefix_visit = tuple(accumulate(visit))
    answer = 0
    for i in range(1, N) :
        cnt = prefix_visit[i]
        ticket = costs[i-1][0]*cnt
        card = costs[i-1][1]*cnt + costs[i-1][2]
        answer += ticket if ticket <= card else card
    return answer

if __name__ == "__main__":
    print(solution())