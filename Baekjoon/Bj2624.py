# 2624 동전 바꿔주기 G5

def solution() :
    T = int(input())
    k = int(input())
    coins = [list(map(int, input().split())) for _ in range(k)]
    D = [0]*(T+1)
    D[0] = 1
    
    for p, n in coins :
        for i in reversed(range(1, T+1)) :
            for j in range(1, n+1) :
                if p*j <= i :
                    D[i] += D[i-p*j]
    return D[-1]

if __name__ == "__main__" :
    print(solution())