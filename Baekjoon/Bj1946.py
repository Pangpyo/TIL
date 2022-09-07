# 1946 신입사원 S1

import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

for _ in range(int(input().rstrip())) :
    N = int(input().rstrip())
    p = []
    for i in range(N) :
        a, b = map(int, input().split())
        p.append((a, b))
    p = sorted(p)
    new = 1
    tmp = p[0][1]
    for i in range(1, N) :
        if tmp > p[i][1] :
            new += 1
            tmp = p[i][1]
    print(new)