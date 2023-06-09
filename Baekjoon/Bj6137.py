# 6137 문자열 생성 G4

import sys


def solution() :
    input = sys.stdin.readline
    N = int(input())
    S = [input().rstrip() for _ in range(N)]
    s = 0
    e = N-1
    T = []
    while s <= e :
        ns = s
        ne = e
        while True :
            if ns >= ne :
                T.append(S[s])
                s += 1
                break
            if S[ns] < S[ne] :
                T.append(S[s])
                s += 1
                break
            elif S[ns] == S[ne] :
                ns += 1
                ne -= 1
            else :
                T.append(S[e])
                e -= 1
                break
    for i, t in enumerate(T) :
        sys.stdout.write(t)
        if (i+1) % 80 == 0 :
            sys.stdout.write("\n") 

if __name__ == "__main__" :
    solution()