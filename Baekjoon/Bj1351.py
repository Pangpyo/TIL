# 1351 무한 수열 G5

A = {0 : 1}

N, P, Q = map(int, input().split())

def findAi(i) :
    p = i//P
    if p not in A :
        findAi(p)
    q = i//Q
    if q not in A :
        findAi(q)
    A[i] = A[p]+A[q]
    return A[i]

if N == 0 :
    print(A[0])
else :
    print(findAi(N))