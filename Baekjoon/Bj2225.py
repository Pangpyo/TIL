# 2225 합분해 G5

def solution() :
    N, K = map(int, input().split())
    D = [[0 if i else 1]*(N+1) for i in range(K)]
    mod = 10**9
    for i in range(1, K) :
        for j in range(N+1) :
            for k in range(N+1) :
                if j+k <= N :
                    D[i][j+k] = (D[i][j+k]+D[i-1][j])%mod
    return D[-1][-1]

if __name__ == "__main__" :
    print(solution())