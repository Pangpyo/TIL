# 2306 유전자 G3

A = list(input())

N = len(A)

ag = {"a": "t", "g": "c"}

D = [[0] * N for _ in range(N)]

for l in range(1, N):
    for i in range(N - l):
        j = i + l
        if A[i] in ag and ag[A[i]] == A[j]:
            D[i][j] = D[i + 1][j - 1] + 2
        for k in range(i, j):
            D[i][j] = max(D[i][j], D[i][k] + D[k + 1][j])

print(D[0][-1])
