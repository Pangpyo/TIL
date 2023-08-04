# 5546 파스타 G4

import sys


def solution() :
    input = sys.stdin.readline
    N, K = map(int, input().split())
    pre = [0]*(N+1)
    for _ in range(K) :
        A, B = map(int, input().split())
        pre[A] = B

    D = [[[0]*4 for _ in range(4)] for _ in range(N+1)]
    D[0][0][0] = 1

    for i in range(1, N+1) :
        for j in range(1, 4) :
            if pre[i] and pre[i] != j :
                continue
            for k in range(4) :
                for y in range(4) :
                    if j == k == y :
                        continue
                    D[i][j][k] += D[i-1][k][y]
                D[i][j][k] %= 10000
    answer = sum(map(sum, D[-1])) % 10000

    return answer

if __name__ == "__main__" :
    print(solution())