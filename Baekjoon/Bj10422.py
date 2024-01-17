# 10422 괄호 G4

def solution() :
    T = int(input())
    MAX = 5000
    D = [0]*(MAX+1)
    D[0] = 1


    MOD = 1_000_000_007
    for i in range(2, MAX+1, 2) :
        for j in range(0, i, 2) :
            D[i] += D[i-j-2] * D[j]
        D[i] %= MOD
    answers = [0]*T

    for t in range(T) :
        answers[t] = D[int(input())]

    return answers

if __name__ == "__main__" :
    print(*solution(), sep='\n')