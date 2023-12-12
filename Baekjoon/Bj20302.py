# 20302 민트 초코 G4

def solution() :
    N = int(input())
    nums = list(input().split())
    MAX = 100_000
    p = [0]*(MAX+1)
    
    cal = '*'
    for i in range(N*2-1):
        if i%2 :
            cal = nums[i]
        else :
            if cal == '*':
                m = 1 
            else :
                m = -1
            n = abs(int(nums[i]))
            if n == 0 :
                return "mint chocolate"
            for i in range(2, int(n**0.5)+1):
                while not n%i :
                    n //= i
                    p[i] += m
            if n > 1 :
                p[n] += m

    for i in range(2, MAX+1) :
        if p[i] < 0 :
            return "toothpaste"
    return "mint chocolate"

if __name__ == "__main__" :
    print(solution())