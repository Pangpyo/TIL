# 2560 짚신벌레 G3

def solution() :
    a, b, d, N = map(int, input().split())
    D = [0]*(N+1)
    D[0] = 1
    adult = 0
    for i in range(N+1) :
        if i - a >= 0 :
            adult += D[i-a]
        if i - b >= 0 :
            adult -= D[i-b]
        D[i] += adult
        D[i] %= 1000
    ans = sum(D[-d::]) % 1000
    return ans

if __name__ == "__main__" :
    print(solution())