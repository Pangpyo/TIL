# 1354 무한수열 2


A = {}
N, P, Q, X, Y = map(int, input().split())


def findAi(i):
    if i <= 0:
        return 1
    if i in A:
        return A[i]
    else:
        A[i] = findAi(i // P - X) + findAi(i // Q - Y)
        return A[i]


print(findAi(N))
