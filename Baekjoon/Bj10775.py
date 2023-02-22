# 10775 공항 G2

import sys

input = sys.stdin.readline

G = int(input())

P = int(input())


gate = list(range(G))
plane = [int(input()) for _ in range(P)]

visit = [0] * G

# print(gate)
def answer():
    cnt = 0
    for p in plane:
        p = p - 1
        while p >= 0:
            np = gate[p]
            if gate[p] < 0:
                return cnt
            if p == gate[p]:
                cnt += 1
                gate[p] -= 1
                break
            else:
                gate[p] -= 1
                p = np
    return cnt


print(answer())
