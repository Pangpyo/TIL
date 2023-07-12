# 2253 점프 G4

import sys


def solution() :
    input = sys.stdin.readline
    N, M = map(int, input().split())
    S = [0]*N
    for _ in range(M) :
        S[int(input())-1] = 1
    mv = int(N**0.5)*2
    inf = sys.maxsize
    D = [[inf]*mv for _ in range(N)]
    D[0][0] = 0
    for i in range(N-1) :
        if S[i] :
            continue
        for j in range(mv) :
            if D[i][j] == inf:
                continue
            for v in [-1, 0, 1] :
                nj = j + v
                ni = i + nj
                if nj < 1 or ni >= N :
                    continue
                D[ni][nj] = min(D[ni][nj], D[i][j]+1)
    ans = min(D[-1])
    return ans if ans != inf else -1

if __name__ == "__main__" :
    print(solution())