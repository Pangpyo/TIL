# 2421 저금통 G5

def solution():
    N = int(input())
    def is_prime(a, b):
        n = int(str(a)+str(b))
        for i in range(2, int(n**0.5) + 1):
            if not n % i:
                return 0
        return 1
    D = [[0]*(N+1) for _ in range(N+1)]
    for i in range(1, N+1):
        for j in range(1, N+1):
            temp = is_prime(i, j)
            D[i][j] = max(D[i][j-1], D[i-1][j]) + temp
    return D[-1][-1] - 1

if __name__ == "__main__":
    print(solution())