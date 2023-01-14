# 7579 앱 G3

n, m = map(int, input().split())

A = list(map(int, input().split()))

C = list(map(int, input().split()))


sc = sum(C)

D = [[0] * (n + 1) for _ in range(sc + 1)]

for i in range(1, sc + 1):
    for j in range(1, n + 1):
        if i >= C[j - 1]:
            D[i][j] = max(D[i][j - 1], D[i - C[j - 1]][j - 1] + A[j - 1])
        else:
            D[i][j] = D[i][j - 1]
    if max(D[i]) >= m:
        print(i)
        break
