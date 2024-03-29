# 24956 나는 정말 휘파람을 못 불어 G4

def solution():
    N = int(input())
    S = input()
    D = [[0, 0, 0, 0] for _ in range(N)]
    WHEE = "WHEE"
    MOD = 1_000_000_007
    for i in range(N) :
        for j in range(4) :
            D[i][j] = D[i-1][j]
            if S[i] == WHEE[j] :
                temp = 0
                if j == 0 :
                    temp = 1
                elif j == 3 :
                    temp = D[i-1][j-1] + D[i-1][j]
                else :
                    temp = D[i-1][j-1]
                D[i][j] = (D[i][j] + temp)%MOD
    return D[-1][-1]

if __name__ == "__main__" :
    print(solution()) 
