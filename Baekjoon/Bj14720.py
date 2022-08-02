# 14720 우유축제 B3

import sys

sys.stdin = open('input.txt')

N = int(input())
milks = list(map(int, input().split()))
def milkstore(n) :
    if n == 0 :
        return 1
    elif n == 1 :
        return 2
    else :
        return 0
drink = 1
try :
    berry = milks.index(0)
except :
    print(0)
    exit(0)
a = milkstore(milks[berry])
for i in range(berry, N) :
    if milks[i] == a :
        drink += 1
        a = milkstore(milks[i])
print(drink)