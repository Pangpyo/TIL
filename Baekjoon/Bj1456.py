# 1456 거의 소수 G5

from math import sqrt, ceil, floor


A, B = map(int, input().split())

a = ceil(sqrt(A))

b = floor(sqrt(B))

che = [False, False] + [True] * (b - 1)
primes = []

for i in range(2, b + 1):
    if che[i]:
        primes.append(i)
        for j in range(2 * i, b + 1, i):
            che[j] = False

ans = 0

for prime in primes:
    i = 2
    while prime**i <= B:
        if prime**i >= A:
            ans += 1
        i += 1
print(ans)
