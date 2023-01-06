# 1209 Sum D3

for t in range(10):
    n = int(input())
    B = [list(map(int, input().split())) for _ in range(100)]
    M = [0, 0, 0]
    for i in range(100):
        row = sum(B[i])
        col = sum([B[j][i] for j in range(100)])
        M[0] += B[i][i]
        M[1] += B[i][-i]
        M.append(max(row, col))
    print(f"#{n} {max(M)}")
