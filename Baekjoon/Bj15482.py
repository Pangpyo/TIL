# 15482 한글 LCS G5

def solitoin() :
    A = input()
    B = input()
    n = len(A)
    m = len(B)
    D = [[0]*(m+1) for _ in range(n+1)]
    for i in range(1, n+1) :
        for j in range(1, m+1) :
            temp = int(A[i-1] == B[j-1])
            D[i][j] = max(D[i-1][j-1] + temp, D[i][j-1], D[i-1][j])
    return D[-1][-1]

if __name__ == "__main__" :
    print(solitoin())