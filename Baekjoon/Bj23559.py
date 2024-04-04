# 23559 밥 G5

import sys


def solution():
    input = sys.stdin.readline
    N, X = map(int, input().split())
    meal = [tuple(map(int, input().split())) for _ in range(N)]
    meal.sort(key = lambda x : (x[1]-x[0]))
    X -= N*1000
    can_buy = X//4000
    buy = 0
    answer = 0
    for i in range(N):
        if buy < can_buy :
            answer += max(meal[i])
            buy += 1
        else :
            answer += meal[i][1]
    return answer

if __name__ == "__main__":
    print(solution())