# 1990 소수인팰린드롬 G5

def solution() :
    a, b = map(int, input().split())
    MAX = 0
    bb = b
    while bb :
        bb //= 10
        MAX += 1
    
    def is_prime(n) :
        for i in range(2, int(n**0.5)+1) :
            if not n%i :
                return False
        return True
    answer = []
    def reverse(n) :
        nn = 0
        while n :
            nn = nn * 10 + n%10
            n //= 10
        return nn

    def palindrome(n, m, d) :
        if m*2 >= d :
            if m*2 > d :
                n = n*(10**(d//2))+reverse(n//10)
            elif m == 1 and d == 1 :
                pass
            else :
                n = n*(10**(d//2))+reverse(n)
            if a<=n<=b and is_prime(n) :
                answer.append(n)
            return
        
        for i in range(10) :
            palindrome(n*10+i, m+1, d)
    
    for d in range(1, MAX+1) :
        for n in range(1, 10, 2) :
            palindrome(n, 1, d)

    answer.append(-1)
    return answer

if __name__ == "__main__" :
    print(*solution(), sep='\n')