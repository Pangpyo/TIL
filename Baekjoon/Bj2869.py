# 2869 달팽이는 올라가고 싶다 S5

from math import ceil


A, B, V = map(int, input().split())

print(ceil((V-A)/(A-B))+1)