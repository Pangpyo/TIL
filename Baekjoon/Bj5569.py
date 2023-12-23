# 5569 출근 경로 G4

def solution() :
    N, M = map(int, input().split())
    r = [[[0, 0, 0, 0, 0] for _ in range(M+1)] for _ in range(N+1)]
    r[1][1][4] = 1
    MOD = 100_000

    for i in range(1, N+1) :
        for j in range(1, M+1) :
            r[i][j][0] += (r[i][j-1][0] + r[i][j-1][2] + r[i][j-1][4]) % MOD
            r[i][j][1] += (r[i-1][j][1] + r[i-1][j][3] + r[i-1][j][4]) % MOD
            r[i][j][2] += (r[i][j-1][1]) % MOD
            r[i][j][3] += (r[i-1][j][0]) % MOD
    return sum(r[-1][-1]) % MOD

if __name__ == "__main__" :
    print(solution())