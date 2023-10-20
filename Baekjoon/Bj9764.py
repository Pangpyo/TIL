# 9764 서로 다른 자연수의 합 G5


def solution() :
    T = int(input())
    ans = [0]*T
    D = [[0 if i else 1 for _ in range(2001)] for i in range(2001)]

    m = 100999
    for i in range(1, 2001) :
        for j in range(1, 2001) :
            if i < j :
                D[i][j] = D[i][j-1]
            else :
                D[i][j] += D[i][j-1] + D[i-j][j-1]
                D[i][j] %= m


    for t in range(T) :
        N = int(input())
        ans[t] = D[N][N]
        
    return ans

if __name__ == "__main__" :
    print(*solution(), sep='\n')