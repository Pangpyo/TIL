# 3114 사과와 바나나 G2
import sys


input = sys.stdin.readline

R, C = map(int, input().split())

ground = [list(input().split()) for _ in range(R)]


apple = [[0] * C for _ in range(R)]
banana = [[0] * C for _ in range(R)]

for j in range(C):
    for i in range(R):
        a = 0
        b = 0
        temp = ground[-(i + 1)][j]
        if temp[0] == "A":
            a += int(temp[1::])
        temp = ground[i][j]
        if temp[0] == "B":
            b += int(temp[1::])
        apple[-(i + 1)][j] = apple[-i][j] + a
        banana[i][j] = banana[i - 1][j] + b

D = [[0] * C for _ in range(R)]

for i in range(C):
    for j in range(R):
        a = 0
        b = 0
        rd = 0
        d = 0
        if j < R - 1:
            a = apple[j + 1][i]
        if j > 0:
            if i > 0:
                b = banana[j - 1][i]
                rd = D[j - 1][i - 1] + a + b
            na = apple[j][i]
            d = D[j - 1][i] + a - na
        r = D[j][i - 1] + a + b
        D[j][i] = max(r, d, rd)


print(D[-1][-1])
