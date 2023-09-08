# 16500 문자열 판별 G5

import sys


def solution() :
    input = sys.stdin.readline
    S = input().rstrip()
    N = int(input())
    A = set(input().rstrip() for _ in range(N))
    L = len(S)
    D = [0]*(L+1)
    D[0] = 1
    for i in range(1, L+1) :
        for word in A :
            l = len(word)
            if i - l >= 0 and D[i-l] and S[i-l:i] == word :
                D[i] = 1
    return D[-1]

if __name__ == "__main__" :
    print(solution())