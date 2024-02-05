# 14718 용감한 용사 진수 G4

import sys


def solution() :
    input = sys.stdin.readline
    N, K = map(int, input().split())
    S = [tuple(map(int, input().split())) for _ in range(N)]

    status = [[0]*3 for _ in range(N)]
    def make_status(n) :
        S.sort(key=lambda x : x[n])
        for i in range(N) :
            status[i][n] = S[i][n]
    for i in range(3) :
        make_status(i)
    S.sort()
    answer = sys.maxsize
    for i in range(N) :
        si = status[i][0]
        for j in range(N) :
            sj = status[j][1]
            for k in range(N) :
                sk = status[k][2]
                use = 0
                for v in range(0, i+1) :
                    if S[v][1] <= sj and S[v][2] <= sk :
                        use += 1
                if use >= K :
                    answer = min(answer, si+sj+sk)

    return answer

if __name__ == "__main__" :
    print(solution())