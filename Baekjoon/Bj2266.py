# 2266 금고 테스트 G2

def solution() :
    N, K = map(int, input().split())
    inf = float('inf')
    K = min(9, K)
    D = [[0]*(N+1) for _ in range(K)]
    for i in range(N+1) :
        D[0][i] = i
    for i in range(1, K) :
        for j in range(1, N+1):
            D[i][j] = inf
            for k in range(1, j+1) :
                D[i][j] = min(D[i][j], max(D[i-1][k-1], D[i][j-k])+1)
    return D[-1][-1]

if __name__ == "__main__" :
    print(solution())