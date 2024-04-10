# 2410 2의 멱수의 합 G5

def solution():
    N = int(input())
    D = [0]*(N+1)
    D[0] = 1
    MOD = 1_000_000_000
    for i in range(1, N+1):
        D[i] = (D[i-2] + D[i//2])%MOD
    return D[N]
if __name__ == "__main__":
    print(solution())