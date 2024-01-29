# 20500 Ezreal 여눈부터 가네 G5

from math import factorial


def solution() :
    N = int(input())
    if N == 1 :
        return 0
    s = 5+N-1
    MOD = 1_000_000_007
    answer = 0

    def permu(a) :
        if a == 0 or a == N-1 :
            return 1
        return factorial(N-1)//(factorial(N-a-1)*factorial(a))


    for i in range(N) :
        ns = s + 4*i
        if ns % 3 == 0 :
            answer = (answer+permu(i))%MOD
    return answer

if __name__ == "__main__" :
    print(solution())