# 5576 콘테스트 B2

import sys

sys.stdin = open('input.txt')
W = []
for _ in range(10) :
    W.append(int(input()))
K = []
for _ in range(10) :
    K.append(int(input()))

W.sort()
K.sort()

print(sum(W[7::]))
print(sum(K[7::]))