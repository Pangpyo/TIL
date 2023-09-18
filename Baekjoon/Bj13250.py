# 13250 주사위 게임 G4

def solution() :
    N = int(input())
    D = [1.0]*(N+1)
    D[1] = 1.0
    for i in range(1, N+1) :
        for j in range(1, 7) :
            if i - j <= 0 :
                continue
            D[i] += D[i-j]/6
    return D[N]

if __name__ == "__main__" :
    print(solution())