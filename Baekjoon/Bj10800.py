# 10800 컬러볼 G3

import sys


def solution():
    input = sys.stdin.readline

    N = int(input())

    balls = []

    for i in range(N):
        c, s = map(int, input().split())
        balls.append([s, c, i])

    balls.sort(key=lambda x: (x[0], x[1]))

    colors = [0] * (N + 1)
    ans = [0] * N

    D = [0] * (N + 1)

    pre = 0
    prec = 0
    presum = 0
    precsum = 0

    for i in range(N):
        s, c, n = balls[i]
        if pre == s:
            presum += pre
            if c == prec:
                precsum += pre
            else:
                precsum = 0
        else:
            presum = 0
            precsum = 0
        D[i + 1] = D[i] + s
        ans[n] = D[i] - colors[c] - presum + precsum
        colors[c] += s
        pre = s
        prec = c
    print(*ans, sep="\n")


if __name__ == "__main__":
    solution()
