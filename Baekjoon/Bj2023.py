# 2023 신기한 소수 G5

N = int(input())

def prime(a) :
    if a < 2 :
        return False
    for i in range(2, int(a**0.5)+1) :
        if a%i == 0 :
            return False
    return True

def dfs(n):
    if len(str(n))==N:
        print(n)
    else:
        for i in range(10):
            temp=n*10+i
            if prime(temp):
                dfs(temp)

dfs(2)
dfs(3)
dfs(5)
dfs(7)