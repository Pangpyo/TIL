# 1958 LCS 3 G3

A = input()
B = input()
C = input()


D = [[[0] * (len(C) + 1) for _ in range(len(B) + 1)] for _ in range(len(A) + 1)]

for i in range(1, len(A) + 1):
    for j in range(1, len(B) + 1):
        for k in range(1, len(C) + 1):
            if A[i - 1] == B[j - 1] == C[k - 1]:
                D[i][j][k] = D[i - 1][j - 1][k - 1] + 1
            else:
                D[i][j][k] = max(
                    D[i][j - 1][k],
                    D[i][j][k - 1],
                    D[i - 1][j][k],
                )

print(D[-1][-1][-1])
