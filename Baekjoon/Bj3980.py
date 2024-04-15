# 3980 선발 명단 G5

import sys


def solution():
    input = sys.stdin.readline
    T = int(input())
    answers = [0]*T
    def dfs(n, power, visit):
        nonlocal answer
        if n == 11:
            answer = max(answer, power)
            return
        for i in range(11):
            if powers[n][i] and not visit&(1<<i):
                dfs(n+1, power + powers[n][i], visit|(1<<i))
    for t in range(T):
        powers = tuple(tuple(map(int, input().split())) for _ in range(11))
        answer = 0
        dfs(0, 0, 0)
        answers[t] = answer
    return answers

if __name__ == "__main__":
    print(*solution(), sep='\n')
