# 15717 떡파이어 G5

def solution():
    N = int(input())
    MOD = 1_000_000_007
    if N == 0:
        return 1
    return pow(2, N-1, MOD)

if __name__ == "__main__":
    print(solution())