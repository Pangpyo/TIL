# 16194 카드 구매하기 2 S1

def solution():
    N = int(input())
    P = tuple(map(int, input().split()))
    INF = float('inf')
    MAX = 1_000
    D = [INF]*(MAX+1)
    D[0] = 0
    for i in range(1, MAX+1):
        for j, p in enumerate(P):
            idx = i-j-1
            if idx >= 0:
                D[i] = min(D[idx] + p, D[i])
    return D[N]

if __name__ == "__main__":
    print(solution())