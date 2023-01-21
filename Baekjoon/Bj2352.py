# 2352 반도체 설계 G2

from bisect import bisect_left as bil


N = int(input())

A = list(map(int, input().split()))
Adp = [A[0]]
for i in range(1, N):
    if Adp[-1] < A[i]:
        Adp.append(A[i])
    else:
        Adp[bil(Adp, A[i])] = A[i]
print(len(Adp))
