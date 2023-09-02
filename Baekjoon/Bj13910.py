# 13910 개업 G5

import sys


def solution() :
    input = sys.stdin.readline
    N, M = map(int, input().split())
    wock = list(map(int, input().split()))
    for i in range(M) :
        for j in range(i+1, M) :
            wock.append(wock[i]+wock[j])
    wock = list(set(wock))
    wock.sort()
    inf = sys.maxsize
    D = [inf]*(N+1)
    D[0] = 0
    for i in range(1, N+1) :
        for w in wock :
            if w <= i and D[i-w] != inf :
                D[i] = min(D[i], D[i-w]+1)
    
    return D[N] if D[N] != inf else -1

if __name__ == "__main__" :
    print(solution())