# 18427 함께 블록 쌓기 G4

def solution() :
    N, M, H = map(int, input().split())
    D = [[0]*(H+1) for i in range(N+1)]
    D[0][0] = 1
    for i in range(1, N+1) :
        for j in map(int, input().split()) :
            for k in range(0, i) :
                for x in range(1, H+1) :
                    if 0 <= x - j <= H and D[k][x - j]:
                        D[i][x] += D[k][x - j]
    ans = sum((D[i][-1] for i in range(N+1)))
    return ans%10007

if __name__ == "__main__" :
    print(solution())