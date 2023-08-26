# 19637 IF문 좀 대신 써줘 S2

import sys


def solution() :
    input = sys.stdin.readline
    N, M = map(int, input().split())
    name = []
    for i in range(N) :
        t, n  = input().split()
        name.append((t, int(n)))

    powers = [(int(input()), i) for i in range(M)]
    name.sort(key = lambda x : x[1])
    powers.sort()
    idx = 0
    ans = ['']*M
    for power, i in powers :
        while name[idx][1] < power :
            idx += 1
        ans[i] = name[idx][0]
    return ans

if __name__ == "__main__" :
    print(*solution(), sep="\n")