# 1563 개근상 G4


def solution() :
    N = int(input())
    D = [[0, 0, 0, 0, 0, 0] for _ in range(N+1)] # 0결, 1결, 2결 / 1지 0결, 1결, 2결
    D[0][0] = 1
    MOD = 1_000_000
    for i in range(1, N+1) :
        D[i][0] = (sum(D[i-1][0:3])) % MOD
        D[i][1] = (D[i-1][0]) % MOD
        D[i][2] = (D[i-1][1]) % MOD
        D[i][3] = (sum(D[i-1])) % MOD
        D[i][4] = (D[i-1][3]) % MOD
        D[i][5] = (D[i-1][4]) % MOD
    return sum(D[-1]) % MOD

if __name__ == "__main__" :
    print(solution())