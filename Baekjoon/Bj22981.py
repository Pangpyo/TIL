# 22981 휴먼 파이프라인 G5

def solution() :
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    V.sort()
    a = V[0]
    b = V[1]
    ans = float('inf')
    for i in range(1, N) :
        b = V[i]
        p = a*i + b*(N-i)
        m = K//p + int(K%p > 0)
        ans = min(ans, m)
    return ans

if __name__ == "__main__" :
    print(solution())