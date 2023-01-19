# 15661 링크와 스타트 S1

from itertools import combinations


N = int(input())

abil = [list(map(int, input().split())) for _ in range(N)]

total = sum(map(sum, abil))

visit = set()

ans = total


def team_abil(team):
    a = 0
    b = 0
    for i in range(len(team)):
        for j in range(len(team)):
            if i == j:
                continue
            a += abil[team[i]][team[j]]
    for i in range(N):
        if i in team:
            continue
        for j in range(N):
            if j in team:
                continue
            b += abil[i][j]
    return abs(a - b)


for i in range(2, N // 2 + 1):
    coms = list(combinations(list(range(N)), i))
    for team in coms:
        ans = min(ans, team_abil(team))


print(ans)
