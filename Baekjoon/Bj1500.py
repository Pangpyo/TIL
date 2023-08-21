# 1500 최대 곱 S2

def solution() :
    S, K = map(int, input().split())
    n = S//K
    m = S%K
    ans = 1
    for i in range(K) :
        ans *= n+1 if i < m else n
    return ans

if __name__ == "__main__" :
    print(solution())