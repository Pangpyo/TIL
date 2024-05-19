# 29704 벼락치기 G5

import sys


def solution():
    input = sys.stdin.readline
    N, T = map(int, input().split())
    probs = [tuple(map(int, input().split())) for _ in range(N)]
    D = [0]*(T+1)
    answer = 0
    for d, m in probs:
        answer += m
        for i in reversed(range(1, T+1)):
            if i - d >= 0:
                D[i] = max(D[i-d]+m, D[i])
    answer -= D[-1]
    return answer

if __name__ == "__main__":
    print(solution())