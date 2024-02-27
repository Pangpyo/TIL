# 14863 서울에서 경산까지 G4

def solution() :
    N, K = map(int, input().split())
    time_fee = tuple(tuple(map(int, input().split())) for _ in range(N))
    
    D = [[-1]*(K+1) for _ in range(N+1)]
    D[0][0] = 0
    for i in range(1, N+1) :
        t1, m1, t2, m2 = time_fee[i-1]
        for j in range(1, K+1) :
            D[i][j] = max(D[i][j], D[i][j-1])
            if j-t1 >= 0 and D[i-1][j-t1] >= 0 :
                D[i][j] = max(D[i][j], D[i-1][j-t1]+m1)
            if j-t2 >= 0 and D[i-1][j-t2] >= 0:
                D[i][j] = max(D[i][j], D[i-1][j-t2]+m2)
    return D[-1][-1]

if __name__ == "__main__" :
    print(solution())