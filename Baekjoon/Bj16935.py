# 16935 배열돌리기3 S1

from pprint import pprint
import sys

sys.stdin = open('input.txt')

N, M, R = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]

def matcal(a) :
    N = len(matrix)
    M = len(matrix[0])
    matrix12 = [[0]*M for _ in range(N)]
    matrix34 = [[0]*N for _ in range(M)]
    if a == 1 :
        for i in range(N) :
            for j in range(M) :
                matrix12[i][j] = matrix[-i-1][j]
        ans = matrix12
    elif a == 2 :
        for i in range(N) :
            for j in range(M) :
                matrix12[i][j] = matrix[i][-j-1]
        ans = matrix12
    elif a == 3 :
        for i in range(M) :
            for j in range(N) :
                matrix34[i][j] = matrix[-j-1][i]
        ans = matrix34
    elif a == 4 :
        for i in range(M) :
            for j in range(N) :
                matrix34[i][j] = matrix[j][-i-1]
        ans = matrix34
    else :
        n = int(N/2)
        m = int(M/2)
        di = [0, 0, n, n]
        dj = [0, m, 0, m]
        mat4 = [[[0]*m for _ in range(n)] for _ in range(4)]

        for k in range(4) :
            for i in range(0, n) :
                for j in range(0, m) :
                    mat4[k][i][j] = matrix[i+di[k]][j+dj[k]]
        nmat4 = []
        if a == 5 :
            for i in range(n) :
                nmat4.append(mat4[2][i]+mat4[0][i])
            for i in range(n) :
                nmat4.append(mat4[3][i]+mat4[1][i])
            ans = nmat4
        elif a == 6 :
            for i in range(n) :
                nmat4.append(mat4[1][i]+mat4[3][i])
            for i in range(n) :
                nmat4.append(mat4[0][i]+mat4[2][i])
            ans = nmat4

    return ans
rotation = list(map(int, input().split()))

for i in rotation :
    matrix = matcal(i)

for i in range(len(matrix)) :
    print(*matrix[i])
