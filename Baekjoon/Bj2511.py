# 2511 카드놀이 B2
import sys
sys.stdin = open("input.txt")

A = list(map(int,input().split()))
B = list(map(int,input().split()))
a = 0
b = 0
winner = 'D'
for i in range(10) :
    if A[i] > B[i] : 
        a += 3
        winner = 'A'
    elif A[i] < B[i] : 
        b += 3
        winner = 'B'
    else : 
        a += 1 
        b += 1
if a > b :
    winner = 'A'
elif a < b :
    winner = 'B'
print(a, b)
print(winner) 
    