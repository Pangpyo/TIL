# 2591 숫자카드 G5

def solution() :
    N = list(map(int, list(input())))
    l = len(N)
    D = [[0, 0] for _ in range(l)]
    
    D[0][0] = 1
    if N[0] == 0 :
        return 0
    for i in range(1, l) :
        if N[i-1] and N[i-1]*10 + N[i] <= 34 :
            D[i][1] = D[i-1][0]
        if N[i] :
            D[i][0] = sum(D[i-1])

    return sum(D[-1])


if __name__ == "__main__" :
    print(solution())