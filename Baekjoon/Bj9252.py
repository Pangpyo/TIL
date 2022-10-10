# 9252 LCS 2 G4


A = input()
B = input()
if len(B) > len(A):
    A, B = B, A
D = [[""] * (len(B) + 1) for _ in range(len(A) + 1)]
for i in range(1, len(A) + 1):
    for j in range(1, len(B) + 1):
        if A[i - 1] == B[j - 1]:
            D[i][j] = "".join([D[i - 1][j - 1], A[i - 1]])
        else:
            D[i][j] = (
                D[i - 1][j] if len(D[i - 1][j]) >= len(D[i][j - 1]) else D[i][j - 1]
            )
a = 0

print(len(D[-1][-1]), D[-1][-1], sep="\n")
