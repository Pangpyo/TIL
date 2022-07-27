# 2846 오르막길 B1
import sys

sys.stdin = open("input.txt")

N = int(input())
Pi = list(map(int, input().split()))
Pi.append(0)
uphill = []
h = []
for i in range(N) :
    uphill.append(Pi[i])
    
    if Pi[i] >= Pi[i+1] :
        h.append(max(uphill)-min(uphill))
        uphill = []

print(max(h))