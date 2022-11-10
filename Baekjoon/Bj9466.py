# 9466 텀 프로젝트 G3

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**5)


def dfs(x, team: list):

    if students[x] <= 0:
        return

    if visit[x]:
        maketeam = False
        for m in team:
            if m == x:
                maketeam = True
            if maketeam:
                students[m] = 0
            else:
                students[m] = -1
        return
    visit[x] = 1
    team.append(x)
    dfs(students[x] - 1, team)


for t in range(int(input())):
    n = int(input())
    students = list(map(int, input().split()))
    visit = [0] * n
    for i in range(n):
        if students[i] > 0:
            dfs(i, [])
    print(n - students.count(0))
