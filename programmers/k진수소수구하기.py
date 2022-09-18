from math import sqrt

def isprime(n) :
    if n == 1 :
        return False
    elif n == 2 :
        return True
    else :
        for i in range(2, int(sqrt(n))+1) :
            if n%i == 0 :
                return False
        return True

def solution(n, k):
    ns = ''
    while n :
        rest = n%k
        n -= rest
        n //= k
        ns = str(rest)+ns
        
    print(ns.split('0'))
    NS = ns.split('0')
    answer = 0
    for s in NS :
        if not s :
            continue
        s = int(s)
        if isprime(s) :
            answer += 1
    
    return answer