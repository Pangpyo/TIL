# 11055 가장 큰 증가부분 수열 S2

N = int(input())

A = list(map(int, input().split()))

D = [n for n in A]

for i in range(N):
    for j in range(i):
        if A[j] < A[i]:
            D[i] = max(D[j] + A[i], D[i])

print(max(D))
