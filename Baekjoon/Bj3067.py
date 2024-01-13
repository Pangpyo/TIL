# 3067 Coins G5

def solution() :
    T = int(input())
    answers = [0]*T
    for t in range(T) :
        N = int(input())
        coins = tuple(map(int, input().split()))
        M = int(input())
        D = [0]*(M+1)
        D[0] = 1
        for coin in coins :
            for i in range(1, M+1) :
                if i - coin >= 0 :
                    D[i] += D[i-coin]
        answers[t] = D[-1]
    return answers

if __name__ == "__main__" :
    print(*solution(), sep='\n')