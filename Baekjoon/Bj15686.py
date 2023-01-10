# 15686 치킨 배달 G5

from itertools import combinations

N, M = map(int, input().split())


chicken = []
houses = []
for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(N):
        if temp[j] == 2:
            chicken.append((i, j))
        elif temp[j] == 1:
            houses.append((i, j))
chickens = list(combinations(chicken, M))


def chickendis(x, y, chicken):  # 가장 가까운 치킨집까지의 거리를 잰다
    ans = 2 * N
    for chi in chicken:
        cx, cy = chi
        ans = min(abs(x - cx) + abs(y - cy), ans)
    return ans


def solution():
    answer = 2 * N * len(houses)
    for chi in chickens:  #
        ans = 0
        for house in houses:  # 집별로 치킨거리를 구한다
            x, y = house
            ans += chickendis(x, y, chi)

        answer = ans if ans < answer else answer
    return answer


print(solution())
