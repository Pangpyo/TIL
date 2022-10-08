# 15686 치킨 배달 G5

from itertools import combinations
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

city = []
chicken = []
houses = []
for i in range(N):
    city.append(list(map(int, input().split())))
    for j in range(N):
        if city[i][j] == 2:
            chicken.append((i, j))
        elif city[i][j] == 1:
            houses.append((i, j))
chickens = list(combinations(chicken, M))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def chickendis(x, y, chicken):
    ans = 2 * N
    for chi in chicken:
        cx, cy = chi
        ans = min(abs(x - cx) + abs(y - cy), ans)
    return ans


def solution():
    answer = 2 * N * len(houses)
    for chi in chickens:
        ans = 0
        for house in houses:
            x, y = house
            ans += chickendis(x, y, chi)

        answer = ans if ans < answer else answer
    return answer


print(solution())
