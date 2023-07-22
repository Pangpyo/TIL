# 17218 비밀번호 만들기 G5

def solution() :
    A = list(input())
    B = list(input())
    n = len(A)
    m = len(B)
    D = [['']*(m+1) for _ in range(n+1)]
    for i in range(1, n+1) :
        for j in range(1, m+1) :
            if len(D[i][j-1]) > len(D[i][j]) :
                D[i][j] = D[i][j-1]
            if len(D[i-1][j]) > len(D[i][j]) :
                D[i][j] = D[i-1][j]
            if A[i-1] == B[j-1] and len(D[i-1][j-1]) + 1 > len(D[i][j]):
                D[i][j] = D[i-1][j-1] + A[i-1]

    return D[-1][-1]

if __name__ == "__main__" :
    print(solution())