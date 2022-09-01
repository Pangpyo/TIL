# 11722 가장 긴 감소하는 부분 수열 S2

N = int(input())

A = (list(map(int, input().split())))
A = A[::-1]
Adp = [1]*N
for i in range(N) :
    for j in range(i) :
        if A[j] < A[i] :
            Adp[i] = Adp[j] + 1 if (Adp[j] + 1) > Adp[i] else Adp[i]
        
print(max(Adp))