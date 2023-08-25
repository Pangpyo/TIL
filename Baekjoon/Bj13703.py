# 13703 물벼룩의 생존확률 G5

def solution() :
    K, N = map(int, input().split())
    D = [[0]*(N+K+1) for _ in range(N+1)]
    D[0][K] = 1
    for i in range(N) :
        for j in range(1, N+K) :
            if not D[i][j] :
                continue
            D[i+1][j+1] += D[i][j]
            D[i+1][j-1] += D[i][j]
    return sum(D[-1][1::])

if __name__ == "__main__" :
    print(solution())