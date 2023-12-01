# 2758 로또 G4

def solution() :
    T = int(input())
    answers = [0]*T
    n = 10
    m = 2000
    D = [[0 if i else j for j in range(m+1)] for i in range(n+1)]
    for i in range(1, n+1) : 
        for j in range(1, m+1) :
            D[i][j] = D[i-1][j//2] + D[i][j-1]
    for t in range(T) :
        N, M = map(int, input().split())
        answers[t] = D[N-1][M]
        
    return answers

if __name__ == "__main__" :
    print(*solution())