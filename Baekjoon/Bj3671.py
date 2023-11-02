# 3671 산업 스파이의 편지 G4

import sys


def solution() :
    input = sys.stdin.readline
    mil = 10000000
    isPrime = [1]*mil
    isPrime[0] = 0
    isPrime[1] = 0
    for i in range(2, mil) :
        if isPrime[i] :
            for j in range(i+i, mil, i) :
                isPrime[j] = 0
    T = int(input())
    answer = [0]*T
    def permutaion(num, cnt) :
        if cnt and isPrime[num] :
            ans.add(num)
        if cnt == N :
            return
        for i in range(l) :
            if used[i] :
                continue
            used[i] = 1
            permutaion(num*10+N[i], cnt+1)
            used[i] = 0
    for t in range(T) :
        N = list(map(int, list(input().rstrip())))
        l = len(N)
        used = [0]*l
        ans = set()
        permutaion(0, 0)
        answer[t] = len(ans)

    return answer

if __name__ == "__main__" :
    print(*solution(), sep='\n')