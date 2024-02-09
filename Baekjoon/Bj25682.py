# 25682 체스판 다시 칠하기 2

import sys


def solution() :
    input = sys.stdin.readline 
    N, M, K = map(int, input().split())
    board = tuple(input().rstrip() for _ in range(N))

    def color(c) :
        sums = [[0]*(M+1) for _ in range(N+1)]
        count = 0
        for i in range(N) :
            for j in range(M) :
                sums[i+1][j+1] = sums[i][j+1] + sums[i+1][j] +int((board[i][j] == c) != (i+j)%2) - sums[i][j]
        for i in range(0, N-K+1) :
            for j in range(0, M-K+1) :
                square = sums[i+K][j+K] - sums[i+K][j] - sums[i][j+K] + sums[i][j]
                count = max(count, square)
                
        return K*K-count
    answer = min(color('B'), color('W'))
    return answer

if __name__ == "__main__" :
    print(solution())