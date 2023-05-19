# 11265 끝나지 않는 파티 G5 

import sys


def solution() :
    input = sys.stdin.readline
    N, M = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(N)]
    for k in range(N) :
        for i in range(N) :
            for j in range(N) :
                if i == j :
                    continue
                D[i][j] = min(D[i][j], D[i][k]+D[k][j])
    ans = []
    yes = "Enjoy other party"
    no = "Stay here"
    for _ in range(M) :
        u, v, d = map(int, input().split())
        if D[u-1][v-1] <= d :
            ans.append(yes)
        else :
            ans.append(no)
    return "\n".join(ans)

if __name__ == "__main__" :
    print(solution())