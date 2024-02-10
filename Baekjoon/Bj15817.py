# 15817 배수 공사 G5

import sys


def solution() :
    input = sys.stdin.readline
    N, x = map(int, input().split())
    pipes = tuple(tuple(map(int, input().split())) for _ in range(N))

    D = [0]*(x+1)
    D[0] = 1

    for l, c in pipes :
        for i in reversed(range(1, x+1)) :
            for a in range(1, c+1) :
                if i-l*a >= 0 and D[i-l*a] :
                    D[i] += D[i-l*a]
    return D[-1]

if __name__ == "__main__" :
    print(solution())