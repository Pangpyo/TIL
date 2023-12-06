# 3933 라그랑주의 네 제곱수 정리 G5

import sys


def solution() :
    input = sys.stdin.readline
    A = 1<<15
    D = [[0, 0, 0, 0] for _ in range(A+1)]
    for i in range(1, int(A**0.5)+1) :
        D[i*i][0] = 1
        for j in range(i*i, A) :
            for k in range(1, 4) :
                D[j][k] += D[j-i*i][k-1]
    answers = []
    while True :
        N = int(input())
        if not N :
            break
        answers.append(sum(D[N]))
    return answers

if __name__ == "__main__" :
    print(*solution(), sep='\n')