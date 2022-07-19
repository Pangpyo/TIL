import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for i in range(1,T+1) :
    A = list(map(int, input().split()))
    a = round(sum(A)/len(A),0)
    print('#%d'%i, '%d'%a)
