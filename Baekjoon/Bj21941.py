# 21941 문자열 제거 G4

import sys


def solution() :
    input = sys.stdin.readline
    S = input().rstrip()
    M = int(input())
    words = []
    for _ in range(M) :
        w, n = input().split()
        words.append((w, int(n), len(w)))
    N = len(S)
    D = [0]*(N+1)
    D[0] = N
    for i in range(1, N+1) :
        D[i] = D[i-1]
        for word, n, l in words :
            if i-l >= 0 and word == S[i-l:i] :
                D[i] = max(D[i-l] + n - l, D[i])
    
    return D[-1]

if __name__ == "__main__" :
    print(solution())