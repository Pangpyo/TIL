# 15989 1, 2, 3 더하기 4 G5

import sys


def solution() :
    input = sys.stdin.readline
    T = int(input())
    D = [0]*10005
    D[0] = 1
    for j in range(1, 4) :
        for i in range(10000) :
            D[i+j] += D[i]
    answer = [0]*T
    for t in range(T) :
        answer[t] = D[int(input())]
    return answer

if __name__ == "__main__" :
    print(*solution(), sep="\n")