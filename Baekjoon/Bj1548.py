# 1548 부분 삼각 수열 G5

def solution() :
    N = int(input())
    B = list(map(int, input().split()))
    B.sort()
    ans = 1
    for i in range(N) :
        a = B[i]
        for j in range(i+1, N) :
            b = B[j]
            temp = 2
            for k in range(j+1, N) :
                c = B[k]
                if a + b > c :
                    temp += 1
                else :
                    break
            ans = max(temp, ans)
    return ans

if __name__ == "__main__" :
    print(solution())