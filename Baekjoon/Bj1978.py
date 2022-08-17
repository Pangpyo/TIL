# 1978 소수 찾기 S5


from math import sqrt
import sys

sys.stdin = open('input.txt')

N = int(input())

primenums = list(map(int, input().split()))

ans = 0

for i in primenums :
    prime = True
    if i == 1 :
        continue
    for j in range(2, int(sqrt(i))+1) :
        if i%j == 0 :
            prime = False
            break
    if prime == True :
        ans += 1
print(ans)
