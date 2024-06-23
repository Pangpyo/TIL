# 25345 루나의 게임 세팅 G5

from math import factorial


def solution():
    N, K = map(int, input().split())
    input()
    MOD = 10**9 + 7
    c = factorial(N)//(factorial(N-K)*factorial(K))*pow(2, K-1, MOD)%MOD
    return c

if __name__ == "__main__":
    print(solution())