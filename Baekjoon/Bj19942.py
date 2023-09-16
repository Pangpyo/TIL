# 19942 다이어트 G5

def solution() :
    N = int(input())
    P, F, S, V = map(int, input().split())
    I = [tuple(map(int, input().split())) for _ in range(N)]
    ans = float('inf')
    U = 0
    def comb(n, p, f, s, v, cost, use) :
        nonlocal ans, U
        if (p >= P and f >= F and s >= S and v >= V) :
            if (ans > cost) :
                ans = cost
                U = use
            return
        for i in range(n, N) :
            comb(i+1, p+I[i][0], f+I[i][1], s+I[i][2], v+I[i][3], cost+I[i][4], use|(1<<i))
    comb(0, 0, 0, 0, 0, 0, 0)
    if ans == float('inf') :
        print(-1)
    else :
        print(ans)
        i = 0
        while (1<<i) <= U :
            if (1<<i) & U :
                print(i+1, end=" ")
            i += 1

if __name__ == "__main__" :
    solution()
