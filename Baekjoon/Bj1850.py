# 1850 최대공약수 S1

from math import gcd


def solution():
    A, B = map(int, input().split())
    N = gcd(A, B)
    return "1"*N

if __name__ == "__main__":
    print(solution())