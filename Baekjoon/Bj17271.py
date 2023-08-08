# 17271 리그 오브 레전설 (small) S1

def solution() :
    N, M = map(int, input().split())
    D = [0]*(N+1)
    D[0] = 1
    mod = 1000000007
    for i in range(1, N+1) :
        D[i] += D[i-1] 
        if i-M >= 0 :
            D[i] += D[i-M]
        D[i] %= mod
    return D[-1]

if __name__ == "__main__" :
    print(solution())