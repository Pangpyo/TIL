# 4097 수익 S2

import sys


def solution():
    input = sys.stdin.readline
    answers = []
    while True:
        N = int(input())
        if not N:
            break
        P = tuple(int(input()) for _ in range(N))
        m = max(P)
        answer = m
        temp = 0
        for e in range(N):
            temp += P[e]
            if temp < 0:
                temp = 0
            elif temp > 0:
                answer = max(answer, temp)
        answers.append(answer)
    return answers

if __name__ == "__main__":
    print(*solution(), sep='\n')