# 2581 소수 S5

from math import sqrt

M = int(input())
N = int(input())


primenums = []

for i in range(M, N+1) :
    prime = True
    if i == 1 :
        continue
    for j in range(2, int(sqrt(i))+1) :
        if i%j == 0 :
            prime = False
            break

    if prime == True :
        primenums.append(i)

if primenums :
    print(sum(primenums), min(primenums))
else :
    print(-1)
