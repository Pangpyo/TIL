# 1058 친구 S2

N = int(input())

inf = N * N + 1

D = [[inf] * N for _ in range(N)]


for i in range(N):
    r = input()
    for j in range(N):
        if i == j:
            D[i][j] = 0
        if r[j] == "Y":
            D[i][j] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            D[i][j] = min(D[i][j], D[i][k] + D[k][j])

ans = 0

for i in range(N):
    cnt = -1
    for j in range(N):
        if D[i][j] <= 2:
            cnt += 1
    ans = max(cnt, ans)

print(ans)
