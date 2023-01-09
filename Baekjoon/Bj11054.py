# 11054 가장 긴 바이토닉 부분 수열 G4

N = int(input())

A = list(map(int, input().split()))
U = [1] * N
D = [1] * N
for i in range(N):
    for j in range(i):
        if A[j] < A[i]:
            U[i] = U[j] + 1 if (U[j] + 1) > U[i] else U[i]
        if A[-(j + 1)] < A[-(i + 1)]:
            D[-(i + 1)] = (
                D[-(j + 1)] + 1 if (D[-(j + 1)] + 1) > D[-(i + 1)] else D[-(i + 1)]
            )

ans = 0
for i in range(N):
    ans = max(U[i] + D[i] - 1, ans)

print(ans)
