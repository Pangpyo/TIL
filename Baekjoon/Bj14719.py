# 14719 빗물 G5

def solution() :
    H, W = map(int, input().split())
    ans = 0
    B = list(map(int, input().split()))

    for i in range(1, H+1) :
        flag = False
        temp = 0
        for j in range(W) :
            if B[j] >= i :
                flag = True
                ans += temp
                temp = 0
            else :
                if flag :
                    temp += 1
    return ans

if __name__ == "__main__" :
    print(solution())