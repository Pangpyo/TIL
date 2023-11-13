# 17845 수강 과목 G5

import sys


def solution() :
    input = sys.stdin.readline
    N, K = map(int, input().split())
    D = [0]*(N+1)
    subs = [tuple(map(int, input().split())) for _ in range(K)]
    for p, t in subs :
        for i in reversed(range(1, N+1)) :
            if i - t >= 0 :
                D[i] = max(D[i-t]+p, D[i])
    return D[-1]

if __name__ == "__main__" :
    print(solution())