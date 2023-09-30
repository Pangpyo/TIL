# 28706 럭키 세븐 G5

import sys


def solution() :
    input = sys.stdin.readline
    T = int(input())
    ans = ["UNLUCKY"]*T
    def operate(n, op, v) :
        if op == '+' :
            return (n+int(v))%7
        else :
            return (n*int(v))%7
    for t in range(T) :
        N = int(input())
        D = [[0]*7 for _ in range(N+1)]
        D[0][1] = 1
        for i in range(1, N+1) :
            op1, v1, op2, v2 = input().split()
            for j in range(7) :
                if D[i-1][j] :
                    D[i][operate(j, op1, v1)] = 1
                    D[i][operate(j, op2, v2)] = 1
        if D[-1][0] :
            ans[t] = "LUCKY"
    return ans

if __name__ == "__main__" :
    print(*solution(), sep='\n')