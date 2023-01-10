# 11054 가장 긴 바이토닉 부분 수열 G4

N = int(input())

A = list(map(int, input().split()))
U = [1] * N # 증가하는 부분수열의 최대 길이
D = [1] * N # 감소하는 부분수열의 최대 길이
for i in range(N):
    for j in range(i):
        if A[j] < A[i]: # 증가하는 부분은 처음부터 세어준다
            U[i] = U[j] + 1 if (U[j] + 1) > U[i] else U[i]
        if A[-(j + 1)] < A[-(i + 1)]: # 감소하는부분은 가장 끝부터 세어준다
            D[-(i + 1)] = (
                D[-(j + 1)] + 1 if (D[-(j + 1)] + 1) > D[-(i + 1)] else D[-(i + 1)]
            )

ans = 0
for i in range(N): # 둘을 더한 값이 가장 높은것이 답
    ans = max(U[i] + D[i] - 1, ans)

print(ans)
