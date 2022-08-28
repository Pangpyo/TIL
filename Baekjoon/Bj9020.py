# 9020 골드바흐의 추측 S2

import sys
sys.stdin = open('input.txt')

from math import sqrt

def primecheck(x) :
    for i in range(2, int(sqrt(x))+1) :
        if x%i == 0 :
            return False
    return True
cases = []
for _ in range(int(input())) :
    cases.append(int(input()))
    primes = []
for i in range(2, max(cases)+1) :
    if primecheck(i) :
        primes.append(i)

for case in cases :
    ans = ()
    for prime in primes :
        if prime > case/2 :
            break
        if case-prime in primes :
            ans = (prime, case-prime)
        
    print(*ans)
